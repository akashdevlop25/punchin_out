from django.db import models
# from django.conf import settings

# Create your models here.

class EmployeeDitels(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField(auto_now_add= True)
    punch_in = models.BooleanField(default=False)
    punch_in_time = models.DateTimeField(blank=True, null=True)
    date = models.DateField(auto_now_add= True)
    punch_out = models.BooleanField(default=False)
    punch_out_time = models.DateTimeField(blank=True, null=True)