from django.db import models

# Create your models here.
class Job(models.Model):
    jobid=models.IntegerField()
    jobtype=models.CharField(max_length=150)


class Worker(models.Model):
    jobid=models.IntegerField()
    wname=models.CharField(max_length=200)
    wphnno=models.IntegerField()
    experience=models.IntegerField()
    gender=models.CharField(max_length=1)
    location=models.CharField(max_length=200)
    specialisation=models.CharField(max_length=200)

    
