from django.conf.urls import include, url
from django.contrib import admin
from pk.views import HomeView,Home2View,ProfileView,MissionView,GalleryView,QualityView,ContactView,AdminView, GitView,TwitterView,FacebookView,SignupView#,LoginView

from pk import views


urlpatterns=[
	url(r'^home/',HomeView.as_view(),name="home"),
	url(r'^home2/',Home2View.as_view(),name="home2"),
	url(r'^adminhome/',AdminView.as_view(),name="adminhome"),
	url(r'^git/',GitView.as_view(),name="git"),
	url(r'^twitter/',TwitterView.as_view(),name="twitter"),
	url(r'^facebook/',FacebookView.as_view(),name="facebook"),
	#url(r'^login/',LoginView.as_view(),name="login"),
	url(r'^login/',views.login,name="login"),
	
        url('^', include('django.contrib.auth.urls')),


	url(r'^profile/',ProfileView.as_view(),name="profile"),
	url(r'^mission/',MissionView.as_view(),name="mission"),
	url(r'^gallery/',GalleryView.as_view(),name="gallery"),
	#url(r'^kids/',KidsView.as_view(),name="kids"),
	#url(r'^family/',FamilyView.as_view(),name="family"),
	#url(r'^toys/',ToysView.as_view(),name="toys"),
	url(r'^quality/',QualityView.as_view(),name="quality"),
	url(r'^contact/',ContactView.as_view(),name="contact"),
	url(r'^signup/$', SignupView.as_view(), name='signup'),



	
]
