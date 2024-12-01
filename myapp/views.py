from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *


# Create your views here.


def home(request):
    return render(request,'home.html')

def djangoform(request):
    x=form_form()
    if request.method =='POST':
        x=form_form(request.POST)
        if x.is_valid():
            x.save()
            return HttpResponse('successfully summited')
    return render(request,'form.html',{'x':x})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def empform(request):
    z=employe_form()
    if request.method =='POST':
        z=employe_form(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse('employee details summited')
    return render(request,'form1.html')


def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = int(request.POST.get('age'))  # Convert to integer
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        obj=student(name=name,age=age,mail=email,password=password,phone=phone)
        obj.save()
        return HttpResponse(f"successfully summited !name:{name},age:{age},email:{email},password:{password},phone:{phone}")

    return render(request,'login.html')