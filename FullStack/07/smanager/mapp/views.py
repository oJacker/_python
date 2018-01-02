from django.shortcuts import render,redirect,HttpResponse
from mapp import models
from django import views
from django.utils.decorators import  method_decorator
# Create your views here.


class Login(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html',{'msg':''})
    def post(self,request,*args,**kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.Administrator.objects.filter(username = user, password = pwd).count()

        if c :
            # request.session['is_login'] = True
            # request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = '用户名或密码错误'
            return render(request, 'login.html',{'msg': message})

def login(request):
    message = ""
    # v = request.sessiong
    from django.contrib.sessions.backends.db import SessionStore
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.Administrator.objects.filter(username= user, password = pwd)
        if c :
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return  rep
        else:
            message = '用户名或密码错误'
    obj = render(request,'login.html',{'msg':message})

def logout(request):
    request.session.clear()
    return redirect('/login.html')

def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('./login.html')
    return inner

# @auth
def index(request):
    #current_user = request.session.get('username')
    current_user = 'ojacker'
    return render(request,'index.html',{'username':current_user})

@auth
def handle_classes(request):
    if request.method == 'GET':
        current_user = request.session.get('username')

        cls_list = models.Classes.objects.all()
        return  render(request,'classes.html',{'username':current_user,'cls_list':cls_list})
    elif request.method == 'POST':
        # Form表单提交的处理方式
        """
        caption = reuqest.POST.get('caption',None)
        if caption:
            models.Classes.objects.create(caption=caption)
        return redirect('/classes.html') 
        """

        # Ajax
        import json
        response_dict = {'status':True,'error':None,'data':None}
        caption = request.POST.get('caption',None)
        print(caption)
        if caption:
            obj = models.Classes.objects.create(caption= caption)
            response_dict['data'] = {'id' : obj.id, 'caption': obj.caption}
        else:
            response_dict['status'] = False
            response_dict['error'] = '标题不能为空'
        return  HttpResponse(json.dumps(response_dict))
def handle_student(request):
    is_login = request.session.get('is_login')
    if is_login:
        current_user = request.session.get('username')
        return  render(request, 'student.html',{'username':current_user})
    else:
        return redirect('/login.html')
def handle_teacher(request):
    is_login = request.session.get('username')
    if is_login:
        current_user = request.session.get('username')
        return render(request, 'teacher.html',{'username':current_user})
    else:
        return redirect('/login.html')
