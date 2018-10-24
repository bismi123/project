# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pk.models import Customer
#from admi.models import Product
from django.contrib.auth.models import User


# Create your models here.

class Custd(models.Model):
	customer=models.OneToOneField(Customer,on_delete=models.CASCADE,)
	status1=models.CharField(max_length=30)
	create_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user1.username




