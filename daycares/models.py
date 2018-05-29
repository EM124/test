from jsonfield import JSONField
from django.conf import settings
from django.db import models
from addresses.models import Address
from django.urls import reverse

class Daycare(models.Model):
	name  			= models.CharField(max_length=120, null=False, blank=False, unique=True)
	identification_number = models.CharField(max_length=30, blank=True)
	NEQ				= models.CharField(max_length=30, blank=True)
	account_number  = models.CharField(max_length=30, blank=True)
	daycare_address = models.ForeignKey(Address, null=True, blank=True)
	CSST			= models.DecimalField(default=0.68, max_digits=10, decimal_places=6)
	unique_company_taxes	= JSONField(default={'CSST':0.68}, blank=True, null=True)
	unique_employee_taxes	= JSONField(default={}, blank=True, null=True)

	def __str__(self):
		return str(self.id)

	def getName(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse("daycares:detail", kwargs={"id": self.id})