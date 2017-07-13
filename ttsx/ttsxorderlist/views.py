#coding=utf-8
from django.shortcuts import render
from ttsxcart.models import CartInfo
# Create your views here.

#  place_order.html 提交订单页
def place_order(request):
    ids=request.POST.getlist('cartids')
    print '----------------'
    print ids
    cart_list=CartInfo.objects.filter(pk__in=ids)
    context={'cart_list':cart_list}
    return render(request,'orderlist/place_order.html',context)