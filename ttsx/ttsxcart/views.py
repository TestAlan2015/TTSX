#coding=utf-8
from django.shortcuts import render
from models import CartInfo
from django.http import JsonResponse
from django.db.models import Sum
# Create your views here.


#  cart.html 我的购物车页，列出已放入购物车上的商品
def cart(request):
    uid=request.session['uid']
    context={}
    good_list=CartInfo.objects.all().filter(cuser_id=uid)
    context['good_list']=good_list
    return render(request,'cart/cart.html',context)
# 添加到购物车
def add(request):
    try:
        uid=request.session['uid']
        pid=request.GET.get('gid')
        count=request.GET.get('count',1)
        goods=CartInfo.objects.all().filter(cuser_id=uid).filter(cproduct_id=pid)
        if len(goods)>0:
            goods[0].count+=1
            goods[0].save()
        else:
            cartinfo=CartInfo()
            cartinfo.count=count
            cartinfo.cproduct_id=pid
            cartinfo.cuser_id=uid
            cartinfo.save()
        return JsonResponse({'save':1})
    except Exception as e:
        print e
        return JsonResponse({'save':0})

# 返回需要的购物车的数据
def count(request):
    uid=request.session['uid']
    count=CartInfo.objects.all().filter(cuser_id=uid).aggregate(Sum('count')).get('count__sum',0)
    return JsonResponse({'count':count})