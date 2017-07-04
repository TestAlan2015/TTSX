#coding=utf-8
from django.shortcuts import render

# Create your views here.

#用户登录
def login(request):
    return render(request,'user/login.html')

#用户注册
def register(request):
    return render(request,'user/register.html')

#用户注册
def info(request):
    return render(request,'user/user_center_info.html')

#用户注册
def order(request):
    return render(request,'user/user_center_order.html')

#用户注册
def site(request):
    return render(request,'user/user_center_site.html')