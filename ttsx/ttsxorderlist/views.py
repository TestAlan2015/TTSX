#coding=utf-8
from django.shortcuts import render

# Create your views here.


def place_order(request):
    return render(request,'orderlist/place_order.html')