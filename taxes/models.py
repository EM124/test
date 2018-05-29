from jsonfield import JSONField
from django.db import models


# Create your models here.
class Tax(models.Model):
	# QPIP_Employee			= models.DecimalField(default=0.00548, max_digits=10, decimal_places=6)
	# QPIP_Employer			= models.DecimalField(default=0.00767,max_digits=10, decimal_places=6)
	# QPP_Employee			= models.DecimalField(default=0.04564,max_digits=10, decimal_places=6)
	# QPP_Employer			= models.DecimalField(default=0.04564, max_digits=10, decimal_places=6)
	# EI_Employee				= models.DecimalField(default=0.013, max_digits=10, decimal_places=6)
	# EI_Employer				= models.DecimalField(default=0.0182, max_digits=10, decimal_places=6)
	# Federal_Income_Tax		= models.DecimalField(default=0.04522, max_digits=10, decimal_places=6)
	# Quebec_Income_Tax		= models.DecimalField(default=0.04283, max_digits=10, decimal_places=6)
	# QHSF_Employer			= models.DecimalField(default=0.023, max_digits=10, decimal_places=6)
	# CNT_Employer			= models.DecimalField(default=0.0007, max_digits=10, decimal_places=6)
	# Vacation_Pay			= models.DecimalField(default=0.04, max_digits=10, decimal_places=6)
	global_company_taxes 	= JSONField(blank=True, null=True, default={'QPIP_Employer':0.00767,'QPP_Employer':0.04564, 'EI_Employer':0.0182, 'QHSF_Employer':0.023,'CNT_Employer':0.0007, 'Vacation_Pay':0.04})
	global_employee_taxes	= JSONField(blank=True, null=True, default={'QPIP_Employee':0.00548, 'QPP_Employee':0.04564,'EI_Employee':0.013, 'Federal_Income_Tax':0.04522, 'Quebec_Income_Tax': 0.04283})
		

	def __str__(self):
		return str(self.id)