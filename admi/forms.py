from django import forms
from admi.models import Custd
from pk.models import Customer
#from admi.models import Product
 

class CustdForm(forms.ModelForm):
	class Meta:
		model=Customer
		exclude=('created_date',)




