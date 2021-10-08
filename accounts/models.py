from django.db import models

# Create your models here.
class NewUser(models.Model):
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=200)
    pwd=models.CharField(max_length=150)
    gender=models.CharField(max_length=1)
    
