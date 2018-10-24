from django import forms
from product.models import Product

class ProductForm(forms.ModelForm):

	class Meta:
		model=Product
		fields=['pro_id','pro_name','pro_details','pro_price','pro_image']
		success_url='success'




