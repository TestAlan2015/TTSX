from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'product/index.html')

def detail(request):
    return render(request,'product/detail.html')

def list(request):
    return render(request,'product/list.html')