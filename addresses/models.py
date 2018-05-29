from django.db import models

# Create your models here.
class Address(models.Model):
	address_line_1  = models.CharField(max_length=120)
	address_line_2  = models.CharField(max_length=120, default="")
	city			= models.CharField(max_length=120)
	country			= models.CharField(max_length=120, default='Canada')
	province		= models.CharField(max_length=120)
	postal_code		= models.CharField(max_length=120)
	home_phone		= models.CharField(max_length=120, default="123 456 7890")
	cell_phone		= models.CharField(max_length=120, default="123 456 7890")

	def __str__(self):
		return str(self.id)