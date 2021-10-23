from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class NewUser(models.Model):
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=200)
    pwd=models.CharField(max_length=150)
    gender=models.CharField(max_length=1)
    def user_test(self, NewUser):
            return self.filter(user=NewUser, viewed=False)

class BookForm(models.Model):
    name=models.CharField(max_length=150)
    mainarea=models.CharField(max_length=150,default='80 Feet Road')
    specialisation=models.CharField(max_length=150, default='Repairs & Fixes')
    phnno=PhoneNumberField( null = False, blank = False)
    addressline1=models.CharField(max_length=150)
    pincode=models.IntegerField()
