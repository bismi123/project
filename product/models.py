# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Product(models.Model):
	pro_id=models.IntegerField()
	pro_name=models.CharField(max_length=20)
	pro_details=models.TextField(validators=[MaxLengthValidator(500)])
	pro_price=models.DecimalField(max_digits=10,decimal_places=2)
	pro_image=models.ImageField(upload_to='media/pic/')
	#created_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.pro_name
