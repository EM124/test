from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .forms import LoginForm, RegisterForm, UpdateForm
from addresses.forms import AddressForm
from daycares.forms import DaycareForm
from worklogs.forms import WorklogForm
from kids.forms import KidForm
from accounts.models import User
from addresses.models import Address
from daycares.models import Daycare
from worklogs.models import Worklog
from kids.models import Kid
from django.http import HttpResponseRedirect
import datetime

def home_page(request):
	context=None
	if request.user.is_authenticated():
		worklog = WorklogForm(request.POST or None)
		
		if worklog.is_valid():
			if request.POST:
				worklog_user = Worklog()
				worklog_user.user = User.objects.get(id=request.user.id)
				split_date = request.POST['date'].split("/")
				correct_date =split_date[2] + "-" + split_date[0]+"-"+split_date[1] 
				worklog_user.hours = worklog.cleaned_data['hours']
				worklog_user.time = correct_date
				worklog_user.save()
				return redirect("/home/")

		today = datetime.date.today()
		weekday = today.weekday()
		start_delta = datetime.timedelta(days=weekday)
		start_of_week = today - start_delta
		week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]
		all_hours_user = Worklog.objects.all().filter(user=request.user.id ,time__range=(week_dates[0], week_dates[6]))
		print(all_hours_user)
		context = {"worklog": worklog,
		"week_dates": week_dates,
		"hours": all_hours_user
		}

	else:
		return redirect("/login/")

	return render(request, "accounts/home.html", context)

class UserDetail(DetailView):
	queryset = User.objects.all()
	template_name = "accounts/detail.html"

	def post(self, request, **kwargs):
		request = self.request
		slug = self.kwargs.get('id')
		instance = User.objects.get(id=slug, active=True)
		address = Address.objects.get(id=instance.user_address.id)
		form = UpdateForm(request.POST or None, initial={'email': instance.email, 'adult_first_name': instance.adult_first_name, 'adult_last_name': instance.adult_last_name } )
		form.fields['email'].widget.attrs['readonly'] = True
		address = AddressForm(request.POST or None, initial={
			'address_line_1': address.address_line_1,
			'address_line_2': address.address_line_2,
			'city': address.city,
			'country': address.country,
			'province': address.province,
			'postal_code': address.postal_code,
			'home_phone': address.home_phone,
			'cell_phone': address.cell_phone,
			 })
		daycare = DaycareForm(request.user)
		data_dicts = Kid.objects.all().filter(parent=slug)
		data_test = [{"id": KidForm(request.POST or None, initial={'child_first_name': data.child_first_name,'child_last_name': data.child_last_name, 'gender': data.gender }), "child_first_name": data.child_first_name,"child_last_name": data.child_last_name, "gender": data.gender} for data in data_dicts]
		selected = [instance.daycare]
		profile_user= {'admin': instance.admin, 'manager': instance.manager, 'employee': instance.employee, 'parent': instance.parent}
		context = {
			"form": form,
			"address": address,
			"daycare": daycare,
			"data_dicts": data_test,
			"selected": selected,
			"profile_user": profile_user,
		}
		if request.POST:
			name_age_pairs = zip(request.POST.getlist('child_first_name'),request.POST.getlist('child_last_name'), request.POST.getlist('gender'))
			
			profile = User.objects.get(id=slug, active=True)
			profile.adult_first_name = request.POST.get("adult_first_name")
			profile.adult_last_name = request.POST.get("adult_last_name")
			if request.POST['choices']=='admin':
				profile.active = True
				profile.admin = True
				profile.staff = True
				profile.manager = False
				profile.employee = False
				profile.parent = False
			elif request.POST['choices']=='manager':
				profile.active = True
				profile.admin = False
				profile.staff = False
				profile.employee = False
				profile.manager = True
				profile.parent = False
			elif request.POST['choices']=='employee':
				profile.active = True
				profile.admin = False
				profile.staff = False
				profile.manager = False
				profile.employee = True
				profile.parent = False
			else:
				profile.active = True
				profile.admin = False
				profile.staff = False
				profile.manager = False
				profile.employee = False
				profile.parent = True

			address_profile = profile.user_address
			address_profile.address_line_1 = request.POST.get("address_line_1")
			address_profile.address_line_2 = request.POST.get('address_line_2')
			address_profile.city = request.POST.get('city')
			address_profile.country = request.POST.get('country')
			address_profile.province = request.POST.get('province')
			address_profile.postal_code = request.POST.get('postal_code')
			address_profile.home_phone = request.POST.get('home_phone')
			address_profile.cell_phone = request.POST.get('cell_phone')
			address_profile.save()
			profile.user_address = address_profile
			profile.save()
			all_selected_daycares = request.POST.getlist('daycare')
			if all_selected_daycares is not None:
				for data in all_selected_daycares:
			 		temporary_daycare = Daycare.objects.get(name=data)
			 		profile.daycare=Daycare.objects.get(id=temporary_daycare.id)

			profile.save()
			if  name_age_pairs is not None:
				data_dicts = [{'child_first_name': child_first_name,'child_last_name': child_last_name, 'gender': gender} for child_first_name, child_last_name, gender in name_age_pairs]
				Kid.objects.all().filter(parent=profile.id).delete()
				for data in data_dicts:
					if data['child_first_name'] != "" and data['child_last_name'] != "":
						profile_kid=Kid()
						profile_kid.parent = profile
						profile_kid.child_first_name=data['child_first_name']
						profile_kid.child_last_name=data['child_last_name']
						profile_kid.gender=data['gender']
						profile_kid.save()	
			return redirect("/register/"+slug)


		return render(request, 'accounts/detail.html', context)

	def get_context_data(self, *args, **kwargs):
		request = self.request
		if request.user.is_authenticated() and (request.user.admin or request.user.manager or request.user.employee):
			context=None
			slug = self.kwargs.get('id')
			if User.objects.filter(id=slug).count() > 0:
				instance = User.objects.get(id=slug, active=True)
			else:
				return context
			address = Address.objects.get(id=instance.user_address.id)
			context = super(UserDetail, self).get_context_data(*args, **kwargs)
			context['form'] = UpdateForm(request.POST or None, initial={'email': instance.email, 'adult_first_name': instance.adult_first_name, 'adult_last_name': instance.adult_last_name } )
			context['form'].fields['email'].widget.attrs['readonly'] = True
			context['profile_user'] = {'admin': instance.admin, 'manager': instance.manager, 'employee': instance.employee, 'parent': instance.parent}
			context['address'] = AddressForm(request.POST or None, initial={
			'address_line_1': address.address_line_1,
			'address_line_2': address.address_line_2,
			'city': address.city,
			'country': address.country,
			'province': address.province,
			'postal_code': address.postal_code,
			'home_phone': address.home_phone,
			'cell_phone': address.cell_phone,
			 })
			context['daycare'] = DaycareForm(request.user)
			data_dicts = Kid.objects.all().filter(parent=slug)
			data_test = [{"id": KidForm(request.POST or None, initial={'child_first_name': data.child_first_name,'child_last_name': data.child_last_name, 'gender': data.gender }), "child_first_name": data.child_first_name,"child_last_name": data.child_last_name, "gender": data.gender} for data in data_dicts]
			context['selected'] = [instance.daycare]
			context['data_dicts'] = data_test
			context['slug'] = slug
			return context
		else:
			redirect("/register/")
	
	def render_to_response(self, context, **response_kwargs):
		request = self.request
		slug = self.kwargs.get('id')
		if context is None:
			return redirect('/register/')
		return super(UserDetail, self).render_to_response(context, **response_kwargs)

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('id')
		#instance = get_object_or_404(User, id=slug, active=True)
		#try:
		instance = None
		if User.objects.filter(id=slug, active=True).count() > 0:
			instance = User.objects.get(id=slug, active=True)
		#print(instance)
		# except Product.DoesNotExist:
		# 	raise Http404("Not found..")
		# except Product.MultipleObjectsReturned:
		# 	qs = Product.objects.filter(slug=slug, active=True)
		# 	instance = qs.first()
		# except:
		# 	raise Http404("Hmm")
		return instance

# def UserDetail(request):
# 	print("test")
# 	#student = get_object_or_404(User, email=id)
# 	return render(request, '/detail.html', {})

def login_page(request):
	if request.user.is_authenticated():
		return redirect("/home/")
	else:
		form = LoginForm(request.POST or None)
		context = {
		"form": form
		}
		next_ = request.GET.get('next')
		next_post = request.POST.get('next')
		redirect_path = next_ or next_post or None
		if form.is_valid():
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			user = authenticate(request, username=email, password=password)
			if user is not None:
				login(request, user)
				if is_safe_url(redirect_path, request.get_host()):
					return redirect(redirect_path)
				else:
					return redirect("/home/")
			else:
				print("Error")

	return render(request, "accounts/login.html", context)

class delete_user(DetailView):
	queryset = User.objects.all()
	template_name = "accounts/register.html"

	def get(self, *args, **kwargs):
		return redirect("/register/")

	def post(self, request, **kwargs):
		request = self.request
		if request.POST and request.user.is_authenticated() and (request.user.admin or request.user.manager or request.user.employee):
			slug = self.kwargs.get('id')
			profile = User.objects.get(id=slug)
			if Kid.objects.all().filter(parent=profile).count() > 0:
				Kid.objects.all().filter(parent=profile).delete()
			profile.delete()
		return redirect("/register/")

def register_page(request):
	if request.user.is_authenticated() and (request.user.admin or request.user.manager or request.user.employee):
		form = RegisterForm(request.POST or None)
		address = AddressForm(request.POST or None)	
		kid = KidForm(request.POST or None)
		instance = None
		if request.user.admin:
			instance = User.objects.all()
		elif request.user.manager:
			instance = User.objects.all().filter(admin=False)

		daycare = DaycareForm(request.user)
		context = {
			"form": form,
			"address": address,
			"daycare": daycare,
			"kid": kid,
			"instance": instance,
		}
		if request.POST:
			if request.POST['choices']=='admin':
				if form.is_valid() and address.is_valid():
					name_age_pairs = zip(request.POST.getlist('child_first_name'),request.POST.getlist('child_last_name'), request.POST.getlist('gender'))
					profile = User()
					profile.email = form.cleaned_data['email']
					profile.set_password(form.cleaned_data["password1"])
					#profile.password = form.cleaned_data['password2']
					profile.adult_first_name = form.cleaned_data['adult_first_name']
					profile.adult_last_name = form.cleaned_data['adult_last_name']
					profile.active = True
					profile.admin = True
					profile.staff = True
					profile.manager = False
					profile.employee = False
					profile.parent = False
					address_profile = Address()
					address_profile.address_line_1 = address.cleaned_data['address_line_1']
					address_profile.address_line_2 = address.cleaned_data['address_line_2']
					address_profile.city = address.cleaned_data['city']
					address_profile.country = address.cleaned_data['country']
					address_profile.province = address.cleaned_data['postal_code']
					address_profile.postal_code = address.cleaned_data['province']
					address_profile.home_phone = address.cleaned_data['home_phone']
					address_profile.cell_phone = address.cleaned_data['cell_phone']
					address_profile.save()
					profile.user_address = address_profile
					profile.save()
					all_selected_daycares = request.POST.getlist('daycare')
					if all_selected_daycares is not None:
						for data in all_selected_daycares:
							temporary_daycare = Daycare.objects.get(name=data)
							profile.daycare.add(temporary_daycare.id)
					profile.save()
					if kid.is_valid() and name_age_pairs is not None:
						data_dicts = [{'child_first_name': child_first_name,'child_last_name': child_last_name, 'gender': gender} for child_first_name,child_last_name, gender in name_age_pairs]
						for data in data_dicts:
							if data['child_first_name'] != "" and data['child_last_name'] != "":
								profile_kid=Kid()
								profile_kid.parent = profile
								profile_kid.child_first_name=data['child_first_name']
								profile_kid.child_last_name=data['child_last_name']
								profile_kid.gender=data['gender']
								profile_kid.save()					
				return redirect("/register/")				
			elif request.POST['choices']=='manager':
				if form.is_valid() and address.is_valid():
					name_age_pairs = zip(request.POST.getlist('child_first_name'),request.POST.getlist('child_last_name'), request.POST.getlist('gender'))
					profile = User()
					profile.email = form.cleaned_data['email']
					profile.set_password(form.cleaned_data["password1"])
					#profile.password = form.cleaned_data['password2']
					profile.adult_first_name = form.cleaned_data['adult_first_name']
					profile.adult_last_name = form.cleaned_data['adult_last_name']
					profile.active = True
					profile.admin = False
					profile.staff = False
					profile.employee = False
					profile.manager = True
					profile.parent = False
					address_profile = Address()
					address_profile.address_line_1 = address.cleaned_data['address_line_1']
					address_profile.address_line_2 = address.cleaned_data['address_line_2']
					address_profile.city = address.cleaned_data['city']
					address_profile.country = address.cleaned_data['country']
					address_profile.province = address.cleaned_data['postal_code']
					address_profile.postal_code = address.cleaned_data['province']
					address_profile.home_phone = address.cleaned_data['home_phone']
					address_profile.cell_phone = address.cleaned_data['cell_phone']
					address_profile.save()
					profile.user_address = address_profile
					profile.save()
					all_selected_daycares = request.POST.getlist('daycare')
					if all_selected_daycares is not None:
						for data in all_selected_daycares:
			 				temporary_daycare = Daycare.objects.get(name=data)
			 				profile.daycare=Daycare.objects.get(id=temporary_daycare.id)
					profile.save()
					if kid.is_valid() and name_age_pairs is not None:
						data_dicts = [{'child_first_name': child_first_name,'child_last_name': child_last_name, 'gender': gender} for child_first_name,child_last_name, gender in name_age_pairs]
						for data in data_dicts:
							if data['child_first_name'] != "" and data['child_last_name'] != "":
								profile_kid=Kid()
								profile_kid.parent = profile
								profile_kid.child_first_name=data['child_first_name']
								profile_kid.child_last_name=data['child_last_name']
								profile_kid.gender=data['gender']
								profile_kid.save()
				return redirect("/register/")
			elif request.POST['choices']=='employee':
				if form.is_valid() and address.is_valid():
					name_age_pairs = zip(request.POST.getlist('child_first_name'),request.POST.getlist('child_last_name'), request.POST.getlist('gender'))
					profile = User()
					profile.email = form.cleaned_data['email']
					profile.set_password(form.cleaned_data["password1"])
					#profile.password = form.cleaned_data['password2']
					profile.adult_first_name = form.cleaned_data['adult_first_name']
					profile.adult_last_name = form.cleaned_data['adult_last_name']
					profile.active = True
					profile.admin = False
					profile.staff = False
					profile.manager = False
					profile.employee = True
					profile.parent = False
					address_profile = Address()
					address_profile.address_line_1 = address.cleaned_data['address_line_1']
					address_profile.address_line_2 = address.cleaned_data['address_line_2']
					address_profile.city = address.cleaned_data['city']
					address_profile.country = address.cleaned_data['country']
					address_profile.province = address.cleaned_data['postal_code']
					address_profile.postal_code = address.cleaned_data['province']
					address_profile.home_phone = address.cleaned_data['home_phone']
					address_profile.cell_phone = address.cleaned_data['cell_phone']
					address_profile.save()
					profile.user_address = address_profile
					profile.save()
					all_selected_daycares = request.POST.getlist('daycare')
					if all_selected_daycares is not None:
						for data in all_selected_daycares:
			 				temporary_daycare = Daycare.objects.get(name=data)
			 				profile.daycare=Daycare.objects.get(id=temporary_daycare.id)
					profile.save()
					if kid.is_valid() and name_age_pairs is not None:
						data_dicts = [{'child_first_name': child_first_name,'child_last_name': child_last_name, 'gender': gender} for child_first_name,child_last_name, gender in name_age_pairs]
						for data in data_dicts:
							if data['child_first_name'] != "" and data['child_last_name'] != "":
								profile_kid=Kid()
								profile_kid.parent = profile
								profile_kid.child_first_name=data['child_first_name']
								profile_kid.child_last_name=data['child_last_name']
								profile_kid.gender=data['gender']
								profile_kid.save()		
				return redirect("/register/")
			elif request.POST['choices']=='parent':
				if form.is_valid() and address.is_valid():
					name_age_pairs = zip(request.POST.getlist('child_first_name'),request.POST.getlist('child_last_name'), request.POST.getlist('gender'))
					profile = User()
					profile.email = form.cleaned_data['email']
					profile.set_password(form.cleaned_data["password1"])
					#profile.password = form.cleaned_data['password2']
					profile.adult_first_name = form.cleaned_data['adult_first_name']
					profile.adult_last_name = form.cleaned_data['adult_last_name']
					profile.active = True
					profile.admin = False
					profile.staff = False
					profile.manager = False
					profile.employee = False
					profile.parent = True
					address_profile = Address()
					address_profile.address_line_1 = address.cleaned_data['address_line_1']
					address_profile.address_line_2 = address.cleaned_data['address_line_2']
					address_profile.city = address.cleaned_data['city']
					address_profile.country = address.cleaned_data['country']
					address_profile.province = address.cleaned_data['postal_code']
					address_profile.postal_code = address.cleaned_data['province']
					address_profile.home_phone = address.cleaned_data['home_phone']
					address_profile.cell_phone = address.cleaned_data['cell_phone']
					address_profile.save()
					profile.user_address = address_profile
					profile.save()
					all_selected_daycares = request.POST.getlist('daycare')
					if all_selected_daycares is not None:
						for data in all_selected_daycares:
			 				temporary_daycare = Daycare.objects.get(name=data)
			 				profile.daycare=Daycare.objects.get(id=temporary_daycare.id)
					profile.save()
					if kid.is_valid() and name_age_pairs is not None:
						data_dicts = [{'child_first_name': child_first_name,'child_last_name': child_last_name, 'gender': gender} for child_first_name,child_last_name, gender in name_age_pairs]
						for data in data_dicts:
							if data['child_first_name'] != "" and data['child_last_name'] != "":
								profile_kid=Kid()
								profile_kid.parent = profile
								profile_kid.child_first_name=data['child_first_name']
								profile_kid.child_last_name=data['child_last_name']
								profile_kid.gender=data['gender']
								profile_kid.save()	
				return redirect("/register/")
			else:
				pass
	else:
		return redirect("/")	
	return render(request, "accounts/register.html", context)
