from django.conf.urls import url
from django.contrib import admin
from admi.views import ListView
from admi import views


urlpatterns=[
	
	url(r'^list/',ListView.as_view(),name="list"),
	#url(r'^pdetail/(?P<pk>[0-9]+)/$',DetailProductView.as_view(),name="pdetail"),
	#url(r'^details2/(?P<pk>[0-9]+)/$',DetailProductView.as_view(),name="details2")
	#url(r'^product/',ProductView.as_view(),name='product'),
	#url(r'^list3/',List3View.as_view(),name="list3"),
	
	
]
