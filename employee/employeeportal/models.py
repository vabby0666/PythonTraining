from __future__ import unicode_literals

from django.db import models
# Create your models here.

class AddEmployee(models.Model):
    username = models.CharField(max_length=120)
    emailId = models.EmailField(max_length=120)
    mobileNumber = models.CharField(max_length=10)
    class Meta:
        unique_together=["emailId"]