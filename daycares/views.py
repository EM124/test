from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from addresses.forms import AddressForm
from daycares.forms import DaycareFormCreation
from accounts.models import User
from addresses.models import Address
from daycares.models import Daycare
from bank.models import Bank
from bank.forms import BankForm
from django.http import HttpResponseRedirect, JsonResponse
from taxes.models import Tax
from django.core import serializers
import datetime

# Create your views here.
def create_daycare(request):
	context=None
	if request.user.is_authenticated() and request.user.admin:
		daycares=Daycare.objects.all()
		daycareform = DaycareFormCreation(request.POST or None)
		address = AddressForm(request.POST or None)
		bank = BankForm(request.POST or None)	
		context={
			'daycare': daycareform,
			'address': address,
			'daycares': daycares,
			'bank': bank
		}

		if request.is_ajax() and request.method == 'GET':
			unique_taxes=Daycare()
			data=[unique_taxes.unique_employee_taxes, unique_taxes.unique_company_taxes]
			return JsonResponse(data, safe=False, content_type='application/json')

		if request.method == 'POST':
			add_daycare(request, daycareform, address, bank)
			return redirect("/daycare/")

	return render(request, "daycares/daycares.html", context)

def add_daycare(request, daycareform, address, bank):
	if daycareform.is_valid():
		daycare=Daycare()
		address_profile=Address()
		bank_checking = Bank()
		bank_credit = Bank()
		daycare.name = request.POST.get('name')
		daycare.identification_number = request.POST.get('identification_number')
		daycare.NEQ = request.POST.get('NEQ')
		daycare.account_number = request.POST.get('account_number')


		#UNIQUE COMPANY TAX
		unique_company_json = {}
		unique_company_name = request.POST.getlist('unique_company')
		unique_company_tax_id = request.POST.getlist('unique_company_tax')
		for index, name in enumerate(unique_company_name):
			unique_company_json[name]=unique_company_tax_id[index]
		daycare.unique_company_taxes=unique_company_json

		#UNIQUE EMPLOYEE TAX
		unique_employee_json = {}
		unique_employee_name = request.POST.getlist('unique_employee')
		unique_employee_tax_id = request.POST.getlist('unique_employee_tax')
		for index, name in enumerate(unique_employee_name):
			unique_employee_json[name]=unique_employee_tax_id[index]
		daycare.unique_employee_taxes=unique_employee_json

		address_profile.address_line_1 = request.POST.get('address_line_1')
		address_profile.address_line_2 = request.POST.get('address_line_2')
		address_profile.city = request.POST.get('city')
		address_profile.country = request.POST.get('country')
		address_profile.province = request.POST.get('postal_code')
		address_profile.postal_code = request.POST.get('province')
		address_profile.home_phone = request.POST.get('home_phone')
		address_profile.cell_phone = request.POST.get('cell_phone')
		address_profile.save()
		daycare.daycare_address = address_profile
		daycare.save()

		#BANK CHECKING
		bank_checking.title = request.POST.get('bank_title')+ "-Checking"
		bank_checking.account_type = 'Checking'
		bank_checking.amount = request.POST.get('checking_amount')
		bank_checking.daycare = daycare
		bank_checking.save()

		#BANK CREDIT
		bank_credit.title = request.POST.get('bank_title') + "-Credit"
		bank_credit.account_type = 'Credit'
		bank_credit.amount = request.POST.get('credit_amount')
		bank_credit.daycare = daycare
		bank_credit.save()

	return None

def detail_daycare(request, id):
	context=None
	if request.user.is_authenticated() and request.user.admin:
		daycare_object = Daycare.objects.get(id=id)
		address=Address.objects.get(id=daycare_object.daycare_address.id)
		bank_checking=Bank.objects.all().filter(daycare=id, account_type='Checking')
		bank_credit=Bank.objects.all().filter(daycare=id, account_type='Credit')
		split_bank_name = bank_checking[0].title.split('-')

		daycareform = DaycareFormCreation(request.POST or None, initial={
			'name': daycare_object.name,
			'identification_number': daycare_object.identification_number,
			'NEQ':daycare_object.NEQ,
			'account_number': daycare_object.account_number,
			})
		addressForm = AddressForm(request.POST or None, initial={
			'address_line_1': address.address_line_1,
			'address_line_2': address.address_line_2,
			'city': address.city,
			'country': address.country,
			'province': address.province,
			'postal_code': address.postal_code,
			'home_phone': address.home_phone,
			'cell_phone': address.cell_phone,
			 })
		bankForm = BankForm(request.POST or None, initial={
			'bank_title': split_bank_name[0],
			'checking_amount': bank_checking[0].amount,
			'credit_amount': bank_credit[0].amount
			 })
		context={
			'daycare': daycareform,
			'address': addressForm,
			'daycare_object': daycare_object,
			'bank': bankForm
		}

		if request.is_ajax() and request.method == 'GET':
			global_tax=Tax.objects.get(id=1)
			daycare_tax=Daycare.objects.get(id=id)
			data=[global_tax.global_company_taxes,global_tax.global_employee_taxes,daycare_tax.unique_company_taxes,daycare_tax.unique_employee_taxes]
			return JsonResponse(data, safe=False, content_type='application/json')

	return render(request, "daycares/detail.html", context)

def update_daycare(request, id):
	context=None
	if request.user.is_authenticated() and request.user.admin:
		daycare_object = Daycare.objects.get(id=id)
		address=Address.objects.get(id=daycare_object.daycare_address.id)
		daycareform = DaycareFormCreation(request.POST or None, initial={
			'name': daycare_object.name,
			'identification_number': daycare_object.identification_number,
			'NEQ':daycare_object.NEQ,
			'account_number': daycare_object.account_number,
			})
		addressForm = AddressForm(request.POST or None, initial={
			'address_line_1': address.address_line_1,
			'address_line_2': address.address_line_2,
			'city': address.city,
			'country': address.country,
			'province': address.province,
			'postal_code': address.postal_code,
			'home_phone': address.home_phone,
			'cell_phone': address.cell_phone,
			 })
		context={
			'daycare': daycareform,
			'address': addressForm,
			'daycare_object': daycare_object,
		}
		if request.method == 'POST':
			edit_daycare(request, id)
			return redirect("/daycare/"+id)
			

	return render(request, "daycares/detail.html", context)

def edit_daycare(request, id):
	daycare=Daycare.objects.get(id=id)
	address_profile=Address.objects.get(id=daycare.daycare_address.id)
	global_tax=Tax.objects.get(id=1)

	bank_checking=Bank.objects.all().filter(daycare=id, account_type='Checking')
	bank_credit=Bank.objects.all().filter(daycare=id, account_type='Credit')

	daycare.name = request.POST.get('name')
	daycare.identification_number = request.POST.get('identification_number')
	daycare.NEQ = request.POST.get('NEQ')
	daycare.account_number = request.POST.get('account_number')
		
	#UNIQUE COMPANY TAX
	unique_company_json = {}
	unique_company_name = request.POST.getlist('unique_company')
	unique_company_tax_id = request.POST.getlist('unique_company_tax')
	for index, name in enumerate(unique_company_name):
		unique_company_json[name]=unique_company_tax_id[index]
	daycare.unique_company_taxes=unique_company_json

	#UNIQUE EMPLOYEE TAX
	unique_employee_json = {}
	unique_employee_name = request.POST.getlist('unique_employee')
	unique_employee_tax_id = request.POST.getlist('unique_employee_tax')
	for index, name in enumerate(unique_employee_name):
		unique_employee_json[name]=unique_employee_tax_id[index]
	daycare.unique_employee_taxes=unique_employee_json

	#GLOBAL COMPANY TAX
	global_company_json = {}
	global_company_name = request.POST.getlist('global_company')
	global_company_tax_id = request.POST.getlist('global_company_tax')
	for index, name in enumerate(global_company_name):
		global_company_json[name]=global_company_tax_id[index]
	global_tax.global_company_taxes=global_company_json

	#GLOBAL EMPLOYEE TAX
	global_employee_json = {}
	global_employee_name = request.POST.getlist('global_employee')
	global_employee_tax_id = request.POST.getlist('global_employee_tax')
	for index, name in enumerate(global_employee_name):
		global_employee_json[name]=global_employee_tax_id[index]
	global_tax.global_employee_taxes=global_employee_json
	

	global_tax.save()
	
	address_profile.address_line_1 = request.POST.get('address_line_1')
	address_profile.address_line_2 = request.POST.get('address_line_2')
	address_profile.city = request.POST.get('city')
	address_profile.country = request.POST.get('country')
	address_profile.province = request.POST.get('postal_code')
	address_profile.postal_code = request.POST.get('province')
	address_profile.home_phone = request.POST.get('home_phone')
	address_profile.cell_phone = request.POST.get('cell_phone')
	address_profile.save()
	daycare.daycare_address = address_profile
	daycare.save()

	#BANK CHECKING
	bank_checking[0].title = request.POST.get('bank_title')+ "-Checking"
	bank_checking[0].amount = request.POST.get('checking_amount')
	bank_checking[0].save()

	#BANK CREDIT
	bank_credit[0].title = request.POST.get('bank_title') + "-Credit"
	bank_credit[0].amount = request.POST.get('credit_amount')
	bank_credit[0].save()
	
	return None



class delete_daycare(DetailView):
	template_name = "daycares/detail.html"

	def get(self, *args, **kwargs):
		return redirect("/daycare/")

	def post(self, request, **kwargs):
		request = self.request
		if request.POST and request.user.is_authenticated() and request.user.admin:
			slug = self.kwargs.get('id')
			daycare = Daycare.objects.get(id=slug)
			Bank.objects.all().filter(daycare=slug).delete()
			Address.objects.get(id=daycare.daycare_address.id).delete()
			daycare.delete()
		return redirect("/daycare/")