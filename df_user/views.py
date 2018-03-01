#coding:utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import JsonResponse ,HttpResponseRedirect
from hashlib import sha1

# Create your views here.

def register(request):
    return render(request,'df_user/register.html')

def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    allow = post.get('allow')

    if pwd != cpwd:
        return redirect('/user/register/')
    s1 = sha1()
    s1.update(pwd)
    upwd = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemail = email
    user.save()
    return redirect('/user/login/')

def info(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    context = {'title':'用户中心','user':user}
    return  render(request,'df_user/info.html',context)

def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.uaddr = post.get('uaddr')
        user.upostnum = post.get('upostnum')
        user.uphone = post.get('uphone')
        user.save()
    context = {'user':user}
    return render(request,'df_user/site.html',context)

def login_handle(request):
    post = request.POST
    uname = post.get('username')
    pwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    user = UserInfo.objects.filter(uname=uname)
    print user
    if len(user) == 1:
        s1 = sha1()
        s1.update(pwd)
        if s1.hexdigest() == user[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,
                       'upwd':pwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname,
                   'upwd': pwd}
        return  render(request,'df_user/login.html',context)
