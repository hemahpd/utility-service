from django.shortcuts import render,redirect
from .models import NewUser
from django.contrib import messages
from django.contrib.auth.models import auth



# Create your views here.



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

def login(request):
    if request.method=="POST":
        try:
            Userdetails=NewUser.objects.get(email=request.POST['email'],pwd=request.POST['pwd'])
            user=auth.authenticate(email=request.POST['email'],pwd=request.POST['pwd'])
            request.session['username']=Userdetails.username
            return render(request,'index.html')
        except NewUser.DoesNotExist as e:
            messages.success(request,'Username/Password Invalid')
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['username']
    except:
        return render(request,'index.html')
    return render(request,'index.html')


def booksuccess(request):
    return render(request,'booksuccess.html')








 





       