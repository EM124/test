from django.db import models
from accounts.models import User
# Create your models here.
class Worklog(models.Model):
	user			= models.ForeignKey(User)
	time			= models.DateTimeField()
	hours			= models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
	def __str__(self):
		return str(self.id)