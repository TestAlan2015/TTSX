
from django.shortcuts import redirect
def islogin(func):
    def new_func(request,*args,**kwargs):
        uname = request.session.get('uname')
        if uname==None:
            return redirect('/user/login')
        return func(request,*args,**kwargs)
    return new_func
