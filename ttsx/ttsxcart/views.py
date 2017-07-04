#coding=utf-8
from django.shortcuts import render

# Create your views here.


#  cart.html 我的购物车页，列出已放入购物车上的商品
def cart(request):
    return render(request,'cart/cart.html')
