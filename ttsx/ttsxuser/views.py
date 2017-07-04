#coding=utf-8
from django.shortcuts import render

# Create your views here.

#  登录页面
def login(request):
    return render(request,'user/login.html')

#  注册页面，已加入了初步的表单验证效果，
def register(request):
    return render(request,'user/register.html')

#  user_center_info.html 用户中心-用户信息页 用户中心功能一，查看用户的基本信息
def info(request):
    return render(request,'user/user_center_info.html')

#  user_center_order.html 用户中心-用户订单页 用户中心功能二，查看用户的全部订单
def order(request):
    return render(request,'user/user_center_order.html')

#  user_center_site.html 用户中心-用户收货地址页 用户中心功能三，查看和设置用户的收货地址
def site(request):
    return render(request,'user/user_center_site.html')