from django.conf.urls import url,include
from django.contrib import admin
from product.views import ProductView,List3View,DetailProductView,KidsView
from product import views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
#from django.contrib.auth import views as auth_views


appname="product"
urlpatterns=[
	url(r'^product/',ProductView.as_view(),name='product'),
	
	url(r'^list3/',List3View.as_view(),name='list3'),
	url(r'^details/(?P<pk>[0-9]+)/$',DetailProductView.as_view(),name='details'),
	url(r'^paypal/', include('paypal.standard.ipn.urls')),
	#url(r'^pay1/',PayView.as_view(),name='pay1'),
	url(r'^payment/$', views.payment, name="payment"),
        url(r'^payment/success$', views.payment_success, name="payment_success"),
        url(r'^payment/failure$', views.payment_failure, name="payment_failure"),
	url(r'^kids/',KidsView.as_view(),name="kids"),


]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
