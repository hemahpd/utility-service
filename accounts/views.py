from django.shortcuts import render,redirect
from .models import NewUser
from django.contrib import messages
from django.contrib.auth.models import auth

# Create your views here.
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        user=auth.authenticate(email=email,pwd=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['pwd']
        gender=request.POST['gender']
        if NewUser.objects.filter(email=email).exists():
                messages.info(request,'Email id taken')
                return redirect('register')
        else:
                NewUser(username=username,email=email,pwd=pwd,gender=gender).save()
                messages.success(request,'Hey,'+request.POST['username']+'. You are registered successfully.')
                return redirect('login')
    else:
        return render(request,'register.html')