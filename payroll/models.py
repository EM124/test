import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from accounts.views import User
from daycare.utils import unique_slug_generator
from django.utils import timezone
from jsonfield import JSONField

# Create your models here.
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1, 9995554243)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return 'payrolls/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)


class Payroll(models.Model):
	user					= models.ForeignKey(User, null=True, blank=True)
	from_time				= models.DateTimeField(null=True)
	to_time					= models.DateTimeField(null=True)
	hours					= models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
	amount_cheque			= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	payed					= models.BooleanField(default=False)
	year						= models.DateTimeField(default=timezone.now)
	proof_of_payement			= models.FileField(upload_to=upload_image_path, null=True, blank=True)
	employee_taxes						= JSONField(default={}, blank=True, null=True)
	company_taxes						= JSONField(default={}, blank=True, null=True)

	def __str__(self):
		return str(self.id)

	def get_year(self):
		return self.year.year

	def get_absolute_url(self):
		return reverse("payrolls:payroll-detail", kwargs={"id": self.id})

# def payroll_pre_save_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)

# pre_save.connect(payroll_pre_save_receiver, sender=Payroll)


