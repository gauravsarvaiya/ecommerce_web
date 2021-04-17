from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import  *
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'top/home.html',{})


def shop_register(request):
    if request.method == 'POST':
        form = shopform(request.POST,request.FILES)
        if form.is_valid():
            form_a = form.save()
            form_a.is_shop = True
            form_a.set_password(form_a.password)
            form_a.save()
            return HttpResponseRedirect(reverse('ecom_app:ecom_login'))
        else:
            print(form.error)
    else:
        form = shopform()
        return render(request,'top/shop_register.html',{'form':form}) 

def customer_register(request):
    if request.method == 'POST':
        form = customerform(request.POST,request.FILES)
        if form.is_valid():
           form_a = form.save()
           form_a.is_customer = True
           form_a.set_password(form_a.password)
           form_a.save()
           return HttpResponseRedirect(reverse('ecom_app:ecom_login'))
        else:
            print(form.errors)
    else:
        form = customerform()
        return render(request,'top/customer_register.html',{'form':form})

def ecom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active and user.is_shop == True:
                   login(request,user)
                   return HttpResponseRedirect(reverse('shop_app:shop_info'))

            elif user.is_active and user.is_customer == True:
                   login(request,user)
                   return HttpResponseRedirect(reverse('customer_app:product_list_show'))
            
            else:
                print('user are not active')
        else:
            print('username and password are worng')
            return HttpResponseRedirect(reverse('ecom_app:ecom_login'))
    else:
        return render(request,'top/ecom_login.html')

def ecom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ecom_app:home'))
            