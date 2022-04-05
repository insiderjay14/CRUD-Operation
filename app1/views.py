from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.conf import path
from app1.models import register

# Create your views here.

def registerview(request):
    if request.method=='POST':
        user=request.POST['username']
        pass1=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        print(user,pass1,email,phone,gender)
        register.objects.create(username=user,password=pass1,email=email,phone=phone,gender=gender)
        return HttpResponse('record is created')
    return render(request,'register.html')

def details(request):
    res=register.objects.all()
    return render(request,'details.html',{'res':res})

def update(request):
    if request.method=='POST':
        user=request.POST['username']
        pass1=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        print(user,pass1,email,phone,gender)
        register.objects.filter(id=1).update(username=user,password=pass1,email=email,phone=phone,gender=gender)
        return HttpResponse('record is updated')
    res=register.objects.get(id=1)
    return render(request,'update.html',{'r':res})

def delete(request):
    if request.method=='POST':
        user=request.POST['userid']
        register.objects.filter(id=user).delete()
        return HttpResponse('record is delete')
    return render(request,'delete.html',)