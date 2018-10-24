# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
#from admi.models import Custd
from admi.forms import CustdForm
from pk.models import Customer
from django.contrib.auth.models import User
#from admi.models import Product

#from admi.forms import ProductForm
# Create your views here.


# Create your views here.

#class OrderView(CreateView):
	#template_name="purchase.html"
	#form_class=OrderForm
	#success_url='success'

class ListView(View):
    model=Customer
    template_name='list2.html'
    context_object_name = 'cust'
    def get(self,request):
        object_list = Customer.objects.all()
        cus = User.objects.all()
        context={
            'cus':cus,
            'object_list':object_list
        }
        return render(request,self.template_name,context)

#class List2View(ListView):
	#model=User
	#template_name="list2.html"


