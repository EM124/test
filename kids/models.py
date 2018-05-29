from django.db import models
from accounts.models import User

# Create your models here.

class Kid(models.Model):
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))	
	child_first_name  = models.CharField(max_length=120, null=False, blank=False)
	child_last_name  = models.CharField(max_length=120, null=False, blank=False)
	parent = models.ForeignKey(User, null=False, blank=False)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	def __str__(self):
		return str(self.child_first_name + " " + self.child_last_name)
