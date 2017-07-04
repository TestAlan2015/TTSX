#coding=utf-8
from django.shortcuts import render

# Create your views here.

#  place_order.html 提交订单页
def place_order(request):
    return render(request,'orderlist/place_order.html')