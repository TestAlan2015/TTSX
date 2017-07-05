#coding=utf-8
from django.shortcuts import render,redirect
from models import UserInfo
from hashlib import sha1
import datetime
# Create your views here.

#  登录页面
def login(request):
    context={}
    context['username']=request.COOKIES['username']
    return render(request,'user/login.html',context)

def login_handle(request):
    post=request.POST
    username=post['username']
    pwd = post['pwd']
    remember=post.get('remember',0)
    s1=sha1()
    s1.update(pwd)
    pwd=s1.hexdigest()

    context={}
    user=UserInfo.objects.filter(uname=username)
    if user.count()>0:
        if pwd==user[0].upassword:
            #request.setsession('uid',username) #设置用户的回话
            response =redirect('/user/info')
            if remember=='1':
                response.set_cookie('username',username,expires=datetime.datetime.now()+datetime.timedelta(14))
            return response
        else:
            context['pwd_error']='密码错误'
            return render(request, 'user/login.html',context)
    else:
        context['user_error'] = '用户名错误'
        return render(request,'user/login.html',context)


#  注册页面，已加入了初步的表单验证效果，
def register(request):
    return render(request,'user/register.html')

# 注册处理类
def user_register_handle(request):
    post= request.POST
    user_name=post['user_name']
    pwd = post['pwd']
    cpwd = post['cpwd']
    email = post['email']
    allow = post.get('allow',0)
    context={'r':post}
    if len(user_name)<5 or len(user_name)>20:
        context['error_name']='用户名需要大于5小于20'
        return render(request,'user/register.html',context)
    elif len(pwd)<5 or len(pwd)>20:
        context['error_pwd'] = '密码需要大于5小于20'
        return render(request, 'user/register.html', context)
    elif pwd!=cpwd:
        context['error_cpwd'] = '两次密码不一致'
        return render(request, 'user/register.html', context)
    elif email.find('@')==-1:
        context['error_email'] = '邮箱格式不正确,请重新输入'
        return render(request, 'user/register.html', context)
    elif allow!='1':
        context['error_allow'] = '邮箱格式不正确,请重新输入'
        return render(request, 'user/register.html', context)
    else:
        use=UserInfo()
        use.uname=user_name
        s1 = sha1()
        s1.update(pwd)
        s1_enctype = s1.hexdigest()
        use.upassword=s1_enctype
        use.umail=email
        use.save()
        return redirect('/user/login')


#  user_center_info.html 用户中心-用户信息页 用户中心功能一，查看用户的基本信息
def info(request):
    return render(request,'user/user_center_info.html')

#  user_center_order.html 用户中心-用户订单页 用户中心功能二，查看用户的全部订单
def order(request):
    return render(request,'user/user_center_order.html')

#  user_center_site.html 用户中心-用户收货地址页 用户中心功能三，查看和设置用户的收货地址
def site(request):
    return render(request,'user/user_center_site.html')

