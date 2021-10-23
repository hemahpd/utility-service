from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Job(models.Model):
    jobid=models.IntegerField()
    jobtype=models.CharField(max_length=150)


class Worker(models.Model):
    jobid=models.IntegerField()
    wname=models.CharField(max_length=200)
    wphnno=PhoneNumberField(unique = True, null = False, blank = False)
    experience=models.IntegerField()
    gender=models.CharField(max_length=1)
    location=models.CharField(max_length=200)
    specialisation=models.CharField(max_length=200)

    
