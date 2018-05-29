from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.core.urlresolvers import reverse
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.views.generic import TemplateView

from daycares.views import (
	create_daycare, 
	detail_daycare,
	delete_daycare, 
	update_daycare
	)

urlpatterns = [
	url(r'^$', create_daycare, name='daycare'),
	url(r'^(?P<id>\d+)/$', detail_daycare, name='detail'),
	url(r'^delete-daycare/(?P<id>\d+)/$', delete_daycare.as_view(), name='delete-daycare'),
	url(r'^update/(?P<id>\d+)/$', update_daycare, name='update-daycare'),
]