from django.db import models
from django.contrib.auth.models import (
		AbstractBaseUser, BaseUserManager
)
from django.urls import reverse
from addresses.models import Address
from daycares.models import Daycare

class UserManager(BaseUserManager):
	def create_user(self, email, adult_first_name=None, adult_last_name=None, user_address=None, daycare=None, password=None, is_active=True, is_employee=False, is_staff=False, is_admin=False):
		if not email:
			raise ValueError("Users mush have an email address")
		if not password:
			raise ValueError("Users must have a password")

		user_obj = self.model(
				email = self.normalize_email(email),
				adult_first_name= adult_first_name,
				adult_last_name = adult_last_name
			)
		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.daycare = daycare
		user_obj.user_address = user_address
		user_obj.employee = is_employee
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, email,adult_first_name=None, adult_last_name=None, password=None):
		user = self.create_user(
				email,
				adult_first_name,
				adult_last_name,
				password=password,
				is_staff=True,
				is_employee=True,
			)
		return user

	def create_superuser(self, email,adult_first_name=None, adult_last_name=None, password=None):
		user = self.create_user(
				email,
				adult_first_name,
				adult_last_name,
				password=password,
				is_staff=True,
				is_employee=True,
				is_admin=True,
			)
		return user

#CustomUser id, password and last_login by default
class User(AbstractBaseUser):
	email = models.EmailField(max_length=255, unique=True)
	adult_first_name = models.CharField(max_length=255, blank=True, null=True)
	adult_last_name = models.CharField(max_length=255, blank=True, null=True)
	salary			= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	active = models.BooleanField(default=True) #can login
	staff = models.BooleanField(default=False) # staff user
	employee = models.BooleanField(default=False)
	manager = models.BooleanField(default=False)
	admin	= models.BooleanField(default=False) # superuser
	timestamp = models.DateTimeField(auto_now_add=True)
	user_address = models.ForeignKey(Address, null=True, blank=True)
	daycare 	 = models.ForeignKey(Daycare, blank=True)
	parent = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] #['full_name']

	objects = UserManager()

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		#return "/accounts/{email}".format(email=self.email)
		return reverse("accounts:update", kwargs={"id": self.id})


	def get_short_name(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_employee(self):
		return self.employee

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_parent(self):
		return self.parent

	@property
	def is_active(self):
		return self.active
