#coding=utf-8
from django.shortcuts import render

# Create your views here.
# index.html   网站首页，顶部“注册|登录”和用户信息是切换显示的，商品分类菜单点击直接链接滚动到本页面商品模块。
def index(request):
    context={'pro':'0'}
    return render(request,'product/index.html',context)

# detail.html  商品详情页，某一件商品的详细信息。
def detail(request):
    context = {'pro': '0'}
    return render(request,'product/detail.html',context)

# list.html  商品列表页，商品分类菜单鼠标悬停时切换显示和隐藏，点击菜单后链接到对应商品的列表页。
def list(request):
    context = {'pro': '0'}
    return render(request,'product/list.html',context)