from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.core.urlresolvers import reverse
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.views.generic import TemplateView

from payroll.views import (
	payroll_information,add_payroll,save_payroll, payroll_detail,delete_payroll
	#payroll_payed
	)

urlpatterns = [
	url(r'^$', payroll_information, name='payroll'),
	url(r'^add-payroll/$', add_payroll, name='add-payroll'),
	#url(r'^payroll_payed/$', payroll_payed, name='payroll-payed'),
	url(r'^save-payroll/$', save_payroll, name='save-payroll'),
	url(r'^delete-payroll/(?P<id>\d+)/$', delete_payroll.as_view(), name='delete-payroll'),
	url(r'^(?P<id>\d+)/$', payroll_detail, name='payroll-detail'),
]