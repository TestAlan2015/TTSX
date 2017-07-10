#coding=utf-8
from django.shortcuts import render
from models import TypeInfo,ProductInfo
from django.core.paginator import Paginator
# Create your views here.
# index.html   网站首页，顶部“注册|登录”和用户信息是切换显示的，商品分类菜单点击直接链接滚动到本页面商品模块。
def index(request):
    context={'pro':'0'}
    list = []

    types=TypeInfo.objects.all()
    for type in types:
        newlist=type.productinfo_set.order_by('-id')[0:4]
        hotlist=type.productinfo_set.order_by('-pprice')[0:4]
        list.append({'newlist':newlist,'hotlist':hotlist,'t':type})
    context['list']=list
    return render(request,'product/index.html',context)

# list.html  商品列表页，商品分类菜单鼠标悬停时切换显示和隐藏，点击菜单后链接到对应商品的列表页。
def list(request,pid,index,orderby):
    desc=request.GET.get('desc')
    t=TypeInfo.objects.get(pk=int(pid))
    new_list=t.productinfo_set.order_by('-id')[0:2]
    paginator=Paginator(t.productinfo_set.order_by('-id'),15)
    if int(orderby) == 2:
        if int(desc)==1:
            paginator = Paginator(t.productinfo_set.order_by('pprice'), 15)
        else:
            paginator = Paginator(t.productinfo_set.order_by('-pprice'), 15)
    elif int(orderby) == 3:
        paginator = Paginator(t.productinfo_set.order_by('-pclick'), 15)
    page=paginator.page(int(index))
    #product的头和其他的页面有区别
    context = {'pro': '0'}
    context['new_list']=new_list
    context['page']=page
    context['t']=t
    context['desc'] = desc
    context['orderby'] = orderby
    # page.
    return render(request,'product/list.html',context)


# detail.html  商品详情页，某一件商品的详细信息。
def detail(request,id):
    #保存点击事件
    product=ProductInfo.objects.get(pk=int(id))
    product.pclick+=1
    product.save()

    #获取浏览记录而且设置
    ids=request.COOKIES.get('browse_list','').split(',')
    if id in ids:
        ids.remove(id)
    ids.insert(0,id)
    if len(ids)>5:
        ids=ids[0:5]
    new_list=product.ptype.productinfo_set.order_by('-id')[0:2]
    context = {'pro': '0'}
    context['product']=product
    context['new_list']=new_list
    httpresponse=render(request,'product/detail.html',context)
    httpresponse.set_cookie('browse_list',','.join(ids),max_age=60*60*24*7)
    return httpresponse



# list.html  商品列表页，商品分类菜单鼠标悬停时切换显示和隐藏，点击菜单后链接到对应商品的列表页。
# def list(request,**kwargs):
#     t=TypeInfo.objects.get(pk=int(kwargs.get('pid',1)))
#     new_list=t.productinfo_set.order_by('-id')[0:2]
#     paginator=Paginator(t.productinfo_set.order_by('-id'),15)
#     page=paginator.page(int(kwargs.get('index')))
#     context = {'pro': '0'}
#     context['new_list']=new_list
#     context['page']=page
#     context['t']=t
#     # page.
#     return render(request,'product/list.html',context)