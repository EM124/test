from django.db import models
from accounts.models import Daycare
# Create your models here.
class Bank(models.Model):
	ACCOUNT_TYPE_CHOICES = (('Checking', 'checking'), ('Credit', 'credit'))
	title  			= models.CharField(max_length=120)
	account_type	= models.CharField(max_length=120, default='Checking', choices=ACCOUNT_TYPE_CHOICES)
	amount			= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	daycare 		= models.ForeignKey(Daycare, null=False, blank=False)


	def __str__(self):
		return str(self.title)