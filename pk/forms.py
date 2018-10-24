from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from pk.models import Customer


class UserCreationForm(UserCreationForm):
	class Meta():
		model=User
                fields=['username','email']
		
class CustomerForm(forms.ModelForm):
	class Meta():
		model=Customer
		fields=['address','nationality']
		
