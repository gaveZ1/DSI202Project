from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from django.contrib import *
from django.contrib.auth.models import User
from django.views.generic import (DetailView,FormView,ListView,TemplateView,UpdateView)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
from django.http import JsonResponse

# Create your views here.




def Register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname =  request.POST.get("firstname")
        lastname =  request.POST.get("lastname")
        email = request.POST.get("email")
        if User.objects.filter(username=username).exists():
            return redirect('/Register')
        elif  User.objects.filter(email=email).exists():
            return redirect('/Register')
        else:
            new_user= User.objects.create_user(username=username,password=password, email=email,first_name=firstname ,last_name=lastname)
            new_user.save()
            auth.login(request,new_user)
            messages.info(request,"Login Sucessful.")
            return redirect('/')
    return render(request, 'CreateAc.html')

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.info(request,"Login Sucuessful") 
                return redirect('/')
            else:
                messages.info(request,"Please login again.") 
                return redirect(request, 'Login.html')
        else:
            messages.info(request,"Please try to login again ") 
            return redirect(request, 'Login.html')
            
    else:
        return render(request, 'Login.html')

def Logout_view(request):
    auth.logout(request)
    return render(request, 'home.html')





def home(request):
    return render(request,'home.html')

def AboutUs(request):
    return render(request,'AboutUs.html')

def payment(request):
    return render(request,'payment.html')

def product(request):
    return render(request,'product.html')

def product1(request):
    return render(request,'product1.html')

def product2(request):
    return render(request,'product2.html')

def profile1(request):
    return render(request,'profile1.html')

def Contact(request):
    return render(request, 'contact.html')
