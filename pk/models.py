# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,)

	address=models.CharField(max_length=10)
	nationality=models.CharField(max_length=10)
	Created_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user.username

