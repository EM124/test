from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from addresses.forms import AddressForm
from daycares.forms import DaycareForm
from payroll.forms import PayrollForm
from payroll.models import Payroll
from worklogs.models import Worklog
from kids.forms import KidForm
from accounts.models import User
from addresses.models import Address
from daycares.models import Daycare
from kids.models import Kid
from taxes.models import Tax
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from bank.models import Bank
import json
from decimal import Decimal

# Create your views here.
def payroll_information(request):
	if request.user.is_authenticated() and request.user.admin:
		allUsers = User.objects.all()
		dates = PayrollForm()
		context = {
		"Users": allUsers,
		"dates": dates
		}
		if request.is_ajax():
			user_id = int(request.GET['id'])
			user_object = User.objects.all().filter(id=user_id)
			daycare = Daycare.objects.all().filter(user=user_object)
			children = Kid.objects.all().filter(parent=user_object)
			address = Address.objects.all().filter(id=user_object[0].user_address.id)
			payroll = Payroll.objects.all().filter(user=user_object)
			tax 	= Tax.objects.all().filter(id=1)

			all_objects =list(user_object) + list(address) + list(daycare) + list(children) + list(payroll) + list(tax)
			data = serializers.serialize('json', all_objects)
				# serialized_obj1 = serializers.serialize('json', user_object)
				# serialized_obj2 = serializers.serialize('json', list(daycare))
				# serialized_obj3 = serializers.serialize('json', list(children))
				# dict = {
				# 	serialized_obj1,
				# 	serialized_obj2,
				# 	serialized_obj3
				# }
				#print(serialized_obj3)
				#user_object = User.objects.get(id=request.GET["id"]).as_json()
			return JsonResponse(data, safe=False, content_type='application/json' )
	else:
		return redirect("/home/")
	return render(request, "payroll/information.html", context)


def add_payroll(request):
	if request.user.is_authenticated() and request.user.admin:
		allUsers = User.objects.all()
		dates = PayrollForm()
		context = {
			"Users": allUsers,
			"dates": dates
		}
		if request.is_ajax():
			user_id = int(request.POST['id'])
			user_object = User.objects.get(id=user_id)
			company_taxes, employee_taxes, hours = calculatePayroll(request)
					
			#payroll = [ Payroll.objects.get(id=new_Payroll.id) ]
			user_object_instance =[user_object,company_taxes,employee_taxes]
			user_object_instance = {
				'id': user_object.id,
				'adult_first_name': user_object.adult_first_name,
				'adult_last_name': user_object.adult_last_name,
				'salary': user_object.salary,
				'hours': hours
			}
			data= [
				user_object_instance,
				company_taxes,
				employee_taxes
			]
			#user_json = serializers.serialize('json', [user_object])
			#data = [user_json]
			#Payroll.objects.get(id=new_Payroll.id).delete()
			return JsonResponse(data, safe=False, content_type='application/json' )
	else:
		return redirect("/home/")
	return render(request, "payroll/information.html", context)

def calculatePayroll(request):
	user_id = int(request.POST['id'])
	user_object = User.objects.get(id=user_id)
	split_date = request.POST['date1'].split("/")
	correct_date =split_date[2] + "-" + split_date[0]+"-"+split_date[1]
	split_date2 = request.POST['date2'].split("/")
	correct_date2 =split_date2[2] + "-" + split_date2[0]+"-"+split_date2[1]
	worklog_time_list = Worklog.objects.filter(user=user_id ,time__range=[correct_date, correct_date2])
	total_time = 0
	for time in worklog_time_list:
		total_time = total_time + time.hours
	
	tax = Tax.objects.get(id=1)
	daycare=Daycare.objects.get(id=user_object.daycare.id)
 
	company_taxes={}
	employee_taxes={}


	if Payroll.objects.all().filter(user=user_id).count() > 0:
		last_Payroll = Payroll.objects.all().filter(user=user_id).order_by('-pk')[0]

		for taxes in tax.global_company_taxes:
			company_taxes[taxes]={
									"Current":round(Decimal(tax.global_company_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2),
									"YTD": round(Decimal(tax.global_company_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary)+Decimal(last_Payroll.company_taxes[taxes]['YTD']), 2)
								}
		for taxes in daycare.unique_company_taxes:
			company_taxes[taxes]= {
									"Current":round(Decimal(daycare.unique_company_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2),
									"YTD":round(Decimal(daycare.unique_company_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary)+Decimal(last_Payroll.company_taxes[taxes]['YTD']), 2)
									}

		employee_taxes["Hourly_Wage"]= { "Current":round(Decimal(total_time)*Decimal(user_object.salary), 2),
											"YTD": round(Decimal(total_time)*Decimal(user_object.salary)+Decimal(last_Payroll.employee_taxes['Hourly_Wage']['YTD']), 2)
										}
		employee_taxes["Cheque_Amount"]=round(Decimal(total_time)*Decimal(user_object.salary), 2)
		for taxes in tax.global_employee_taxes:
			employee_taxes[taxes]={ 
									"Current":round(Decimal(tax.global_employee_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2),
									"YTD":round(Decimal(tax.global_employee_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary)+Decimal(last_Payroll.employee_taxes[taxes]['YTD']), 2)
									}
			employee_taxes['Cheque_Amount']=Decimal(employee_taxes['Cheque_Amount']) - Decimal(employee_taxes[taxes]['Current'])
		for taxes in daycare.unique_employee_taxes:
			employee_taxes[taxes]={'Current':round(Decimal(tax.unique_employee_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2),
									'YTD': round(Decimal(tax.unique_employee_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary)+Decimal(last_Payroll.employee_taxes[taxes]['YTD']), 2)
									}
			employee_taxes['Cheque_Amount']=Decimal(employee_taxes['Cheque_Amount']) - Decimal(employee_taxes[taxes]['Current'])

		employee_taxes['Cheque_Amount']=round(employee_taxes['Cheque_Amount'],2)		
	else:
		for taxes in tax.global_company_taxes:
			company_taxes[taxes]={
									"Current":round(Decimal(tax.global_company_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2),
									"YTD": round(Decimal(tax.global_company_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2)
								}
		for taxes in daycare.unique_company_taxes:
			company_taxes[taxes]= {
									"Current":round(Decimal(daycare.unique_company_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2),
									"YTD":round(Decimal(daycare.unique_company_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2)
									}

		employee_taxes["Hourly_Wage"]= { "Current":round(Decimal(total_time)*Decimal(user_object.salary), 2),
											"YTD": round(Decimal(total_time)*Decimal(user_object.salary), 2)
										}
		employee_taxes["Cheque_Amount"]=round(Decimal(total_time)*Decimal(user_object.salary), 2)
		for taxes in tax.global_employee_taxes:
			employee_taxes[taxes]={ 
									"Current":round(Decimal(tax.global_employee_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2),
									"YTD":round(Decimal(tax.global_employee_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2)
									}
			employee_taxes['Cheque_Amount']=Decimal(employee_taxes['Cheque_Amount']) - Decimal(employee_taxes[taxes]['Current'])
		for taxes in daycare.unique_employee_taxes:
			employee_taxes[taxes]={'Current':round(Decimal(tax.unique_employee_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2),
									'YTD': round(Decimal(tax.unique_employee_taxes[taxes])*Decimal(total_time)*Decimal(user_object.salary), 2)
									}
			employee_taxes['Cheque_Amount']=Decimal(employee_taxes['Cheque_Amount']) - Decimal(employee_taxes[taxes]['Current'])

		employee_taxes['Cheque_Amount']=round(employee_taxes['Cheque_Amount'],2)
	
	return company_taxes, employee_taxes, total_time


def save_payroll(request):
	if request.user.is_authenticated() and request.user.admin:
		if request.is_ajax():
			user_id = int(request.POST['id'])
			user_object = User.objects.all().filter(id=user_id)
			split_date = request.POST['date1'].split("/")
			correct_date =split_date[2] + "-" + split_date[0]+"-"+split_date[1]
			split_date2 = request.POST['date2'].split("/")
			correct_date2 =split_date2[2] + "-" + split_date2[0]+"-"+split_date2[1]
			worklog_time_list = Worklog.objects.filter(user=user_id ,time__range=[correct_date, correct_date2])
			
			hours= float(request.POST['hours'])
			cheque_amount = float(request.POST['cheque_amount'])
			company_taxes = json.loads(request.POST.get('company_taxes'))
			employee_taxes = json.loads(request.POST.get('employee_taxes'))
			#company_taxes = request.POST.get('company_taxes')
			#print(company_taxes)
			#employee_taxes = request.POST.get('employee_taxes')
			#print(employee_taxes)
			new_Payroll = Payroll()
			new_Payroll.user = user_object[0]
			new_Payroll.from_time = correct_date
			new_Payroll.to_time = correct_date2
			new_Payroll.hours = hours
			new_Payroll.amount_cheque = cheque_amount
			new_Payroll.employee_taxes = employee_taxes
			new_Payroll.company_taxes = company_taxes
			new_Payroll.save()
					
					

		payroll = [Payroll.objects.get(id=new_Payroll.id)]
		all_objects =list(user_object) + list(payroll)
		data = serializers.serialize('json', all_objects)
		return JsonResponse(data, safe=False, content_type='application/json')
	else:
		return redirect("/home/")
	return render(request, "payroll/information.html", {})


def payroll_detail(request, id):
	if request.user.is_authenticated() and request.user.admin:
		print(id)
		payroll = Payroll.objects.get(id=id)
		payroll_list = Payroll.objects.all().filter(id=id)
		user = User.objects.get(id=payroll.user.id)
		user_list = User.objects.all().filter(id=payroll.user.id)
		daycare = Daycare.objects.all().filter(id=user.daycare.id)
		bank_accounts = Bank.objects.all().filter(daycare=daycare[0].id)
		context = {
			"payroll": payroll,
			"user": user,
			"banks": bank_accounts,
		}
		if request.is_ajax() and request.method == 'GET':
			print("in")
			all_objects =list(payroll_list) + list(user_list) + list(daycare) + list(bank_accounts)
			data = serializers.serialize('json', all_objects)
			return JsonResponse(data, safe=False, content_type='application/json')
	else:
		return redirect("/home/")
	return render(request, "payroll/detail.html", context)


# def payroll_payed(request):
# 	if request.user.is_authenticated() and request.user.admin:
# 		if request.is_ajax():
# 			payroll_id = int(request.POST['id'])
# 			payroll_true_or_false = request.POST['checkbox']
# 			payroll = Payroll.objects.get(id=payroll_id)
# 			if payroll_true_or_false == 'true':
# 				payroll.payed = True
# 			else:
# 				payroll.payed = False
# 			payroll.save()
# 	else:
# 		return redirect("/home/")
# 	return render(request, "payroll/information.html", {})


class delete_payroll(DetailView):
	template_name = "payroll/detail.html"

	def get(self, *args, **kwargs):
		return redirect("/payrolls/")

	def post(self, request, **kwargs):
		request = self.request
		if request.POST and request.user.is_authenticated() and request.user.admin:
			slug = self.kwargs.get('id')
			Payroll.objects.get(id=slug).delete()
		return redirect("/payrolls/")