from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.views.generic import TemplateView

from accounts.views import login_page, register_page, home_page
#from django.conf.urls.defaults import handler404, handler500
#from app.views import error

urlpatterns = [
	# url(r'^$', home_page, name='home'),
	# url(r'^about/$', about_page, name='about'),
	# url(r'^contact/$', contact_page, name='contact'),
	url(r'^$', login_page, name='login'),
	url(r'^home/$', home_page, name='home'),
	#url(r'^payroll/$', checkout_address_create_view, name='checkout_address_create'),
	# url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
	# url(r'^register/guest/$', guest_register_view, name='guest_register'),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),
	# url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
	# url(r'^cart/', include("carts.urls", namespace='cart')),
	url(r'^register/$', register_page, name='register'),
	url(r'^register/', include("accounts.urls", namespace='accounts')),
	url(r'^payrolls/', include("payroll.urls", namespace='payrolls')),
	url(r'^daycare/', include("daycares.urls", namespace='daycares')),
	# url(r'^search/', include("search.urls", namespace='search')),
    url(r'^admin/', admin.site.urls),
]

#handler404 = error.error_handler

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
