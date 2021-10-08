from django.shortcuts import render

# Create your views here.
def electrician(request):
    return render(request,'electrician.html')

def plumber(request):
    return render(request,'plumber.html')

def cleaner(request):
    return render(request,'cleaner.html')

