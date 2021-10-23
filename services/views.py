import random
from django.shortcuts import render,redirect
from accounts.models import BookForm
from worker.models import Worker
from django.contrib import messages

# Create your views here.
def electrician(request):
    if request.method=="POST":
        name=request.POST['name']
        phnno=request.POST['phnno']
        addressline1=request.POST['addressline1']
        pincode=request.POST['pincode']
        mainarea=request.POST['mainarea']
        specialisation=request.POST['specialisation']
        BookForm(name=name,specialisation=specialisation,phnno=phnno,addressline1=addressline1,pincode=pincode,mainarea=mainarea).save()
        value=Worker.objects.filter(location=mainarea,specialisation=specialisation)
        data=random.choice(value)
        return render(request,'booksuccess.html',{'data':data})
    else:
        return render(request,'electrician.html')

        


def plumber(request):
    if request.method=="POST":
        name=request.POST['name']
        phnno=request.POST['phnno']
        addressline1=request.POST['addressline1']
        pincode=request.POST['pincode']
        mainarea=request.POST['mainarea']
        specialisation=request.POST['specialisation']
        BookForm(name=name,specialisation=specialisation,phnno=phnno,addressline1=addressline1,pincode=pincode,mainarea=mainarea).save()
        value=Worker.objects.filter(location=mainarea,specialisation=specialisation)
        data=random.choice(value)
        return render(request,'booksuccess.html',{'data':data})
    else:
        return render(request,'plumber.html')
    

def cleaner(request):
    if request.method=="POST":
        name=request.POST['name']
        phnno=request.POST['phnno']
        addressline1=request.POST['addressline1']
        pincode=request.POST['pincode']
        mainarea=request.POST['mainarea']
        specialisation=request.POST['specialisation']
        BookForm(name=name,specialisation=specialisation,phnno=phnno,addressline1=addressline1,pincode=pincode,mainarea=mainarea).save()
        value=Worker.objects.filter(location=mainarea,specialisation=specialisation)
        data=random.choice(value)
        return render(request,'booksuccess.html',{'data':data})
    else:
        return render(request,'cleaner.html')


def booking(request):
        value1=BookForm.objects.filter()
        return render(request,'booking.html',{'value1':value1})

def cancelBooking(request):
         cancel=BookForm.objects.last()
         cancel.delete()
         messages.success(request,'Booking cancelled successfully')
         return render(request,'index.html')
         


