from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.core.urlresolvers import reverse
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.views.generic import TemplateView

from accounts.views import (
	UserDetail, delete_user
	)

urlpatterns = [
	url(r'^delete-user/(?P<id>\d+)/$', delete_user.as_view(), name='delete'),
	url(r'^(?P<id>\d+)/$', UserDetail.as_view(), name='update'),
]

