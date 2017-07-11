#coding=utf-8
from django.shortcuts import render,redirect
from models import UserInfo
from hashlib import sha1
import datetime
from django.http import JsonResponse
from ttsxproduct.models import ProductInfo
# Create your views here.
from . import user_decorator


#  登录页面
def login(request):
    context={'top':0}
    context['username']=request.COOKIES.get('username','')
    return render(request,'user/login.html',context)

def loginin(request):
    user=request.session['uid']
    if user is not None:
        return JsonResponse({'ok':1})
    else:
        return JsonResponse({'ok':0})

#  登录页面
def loginout(request):
    request.session.flush()
    return redirect('/user/login')

# 处理用户名异步注册的时候存在问题
def isvalid(request):
    count=UserInfo.objects.filter(uname=request.GET['username']).count()
    if count>0:
        return JsonResponse({'flag':1})
    elif count==0:
        return  JsonResponse({'flag':0})


# 用户的登陆验证
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
            request.session['uid']=user[0].id
            request.session['uname']=user[0].uname #设置用户的回话
            response =redirect(request.session.get('path','/product/index'))
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
    context = {'top': 0}
    return render(request,'user/register.html',context)

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
@user_decorator.islogin
def info(request):
    ids=request.COOKIES.get('browse_list','').split(',')[:-1]
    products=[]
    for id in ids:
        products.append(ProductInfo.objects.get(pk=int(id)))
    context={}

    context['username'] = request.session.get('uname')
    context['products'] = products
    return render(request,'user/user_center_info.html',context)



#  user_center_order.html 用户中心-用户订单页 用户中心功能二，查看用户的全部订单
@user_decorator.islogin
def order(request):
    username = request.session.get('uname')
    return render(request,'user/user_center_order.html',{'username':username})

#  user_center_site.html 用户中心-用户收货地址页 用户中心功能三，查看和设置用户的收货地址
@user_decorator.islogin
def site(request):
    method=request.method
    username = request.session.get('uname')
    user = UserInfo.objects.get(uname=username)

    if method=='GET':
        return render(request, 'user/user_center_site.html',{'user':user,'username':username})
    elif method=='POST':
        post = request.POST
        receiver = post['receiver']
        address = post['address']
        code = post['code']
        phone = post['phone']
        user.ureveiver=receiver
        user.address = address
        user.ucode = code
        user.uphone = phone
        user.save()
        return redirect('/user/site/')
