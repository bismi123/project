# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView
#from pk.forms import SignUpForm
from django.shortcuts import render
from pk.forms import UserCreationForm,CustomerForm
from pk.models import Customer

from django.conf import settings
from django.contrib import messages

from pk.models import Customer
from .forms import CustomerForm

# Create your views here.



class HomeView(TemplateView):
	template_name="home.html"
class Home2View(TemplateView):
	template_name="home2.html"
	
class ProfileView(TemplateView):
	template_name="profile.html"
	
class MissionView(TemplateView):
	template_name="mission.html"
	
class GitView(TemplateView):
	template_name="git.html"
	
class FacebookView(TemplateView):
	template_name="facebook.html"
class TwitterView(TemplateView):
	template_name="twitter.html"

	
class GalleryView(TemplateView):
	template_name="gallery.html"


#class LoginView(TemplateView):
#	template_name="login.html"
class QualityView(TemplateView):
	template_name="quality.html"
class ContactView(TemplateView):
	template_name="contact.html"
class AdminView(TemplateView):
	template_name="adminhome.html"



	

#@login_required
#def home(request):
#    return render(request, 'login.html')

def login(request):
     form =AuthenticationForm()
     if request.user.is_authenticated():
         if request.user.is_superuser:
             return redirect("/adminhome/")# or your url name
         if request.user.is_staff:
             return redirect("/kids/")# or your url name


     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = auth.authenticate(username=username, password=password)

         if user is not None:
             # correct username and password login the user
             auth.login(request, user)
             if request.user.is_superuser:
                 return redirect("/adminhome/")# or your url name
             if request.user.is_staff:
                 return redirect("/kids/")# or your url name

         else:
             messages.error(request, 'Error wrong username/password')
     context = {}
     context['form']=form

     return render(request, 'login.html', context)



@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
     context = {}
     return render(request, 'kids.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
     context = {}
     return render(request, 'adminhome.html', context)




class SignupView(FormView):
	template_name="signup.html"
	form_class=UserCreationForm
	model=Customer

	def get(self, request, *args, **kwargs):
		self.object=None
		form_class=self.get_form_class()
		user_form = self.get_form(form_class)
		cust_form=CustomerForm()
		return self.render_to_response(self.get_context_data
		(form1=user_form,form2=cust_form))

	def post(self, request, *args, **kwargs):
		self.object=None
		form_class=self.get_form_class()
		user_form = self.get_form(form_class)
		cust_form=CustomerForm(self.request.POST,self.request.FILES)
		if(user_form.is_valid() and cust_form.is_valid()):
			return self.form_valid(user_form,cust_form)
		else:
			return self.form_invalid(user_form,cust_form)
		
	def form_valid(self, user_form, cust_form):
		self.object = user_form.save()
		self.object.is_staff=True
		self.object.save()
		p = cust_form.save(commit=False)
		p.user = self.object
		p.save()	

	def form_invalid(self, user_form, cust_form):
		return self.render_to_response(self.get_context_data(form1=user_form,form2=cust_form))	
