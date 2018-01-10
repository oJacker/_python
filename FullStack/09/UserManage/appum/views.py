from django.shortcuts import render,redirect,HttpResponse
from appum import  models
# Create your views here.


'''
def login(request):
    message = ""
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Admiinistrator.objects.filter(username = user, password= pwd).count()
        if c:
            rep = redirect('/index.html')
            rep.set_signed_cookie('username',user)
            rep.set_signed_cookie('account','123123123')
            rep.set_signed_cookie('pwd','admin123456')
            return rep
        else:
            message = '用户名或密码错误'
    return render(request,'login.html',{'msg':message})

def index(request):
    # 如果用户已经登录，获取当前登录的用户名
    # 否则，返回登录页面
    username = request.get_signed_cookie('username')
    if username:
        return render(request, 'index.html',{'username':username})
    else:
        return redirect('/login.html')
'''

from django import views
from django.utils.decorators import method_decorator

class Login(views.View):
    def get(self,request, *args, **kwargs):
        return render(request, 'login.html',{'msg':''})

    def post(self,request,*args, **kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Administrator.objects,filter(username =user, password = pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误"
            return render(request,"login.html",{'msg':message})


def login(request):
    message = ""
    v = request.session
    print(type(v))
    from django.contrib.sessions.backends.db import SessionStore

    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Administrator.objects.filter(username= user, password= pwd).count()

        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
        else:
            message = "用户名或密码错误"
    obj =  render(request,'login.html',{'msg':message})
    return obj

def logout(request):
    request.session.clear()
    return redirect('/login.html')


def auth(func):
    def inner(request, *args, **kwargs):
        is_login= request.session.get('is_login')
        if is_login:
            return func(request,*args,**kwargs)
        else:
            return redirect('/login.html')
    return inner

@auth
def index(request):
    current_user = request.session.get('username')
    return render(request, 'index.html',{'username':current_user})

@auth
def handle_classes(request):
    if request.method == "GET":
        current_user = request.session.get('username')


        #cls_list = models.Classes.objects.all()
        #return (request,'classes.html',{'username':current_user,'cls_list':cls_list})

        current_page = request.GET.get('p',1)
        current_page = int(current_page)
        print(current_page)
        # 所有数据的个数
        total_count = models.Classes.objects.all().count()

        from utils.page import PagerHelper
        obj = PagerHelper(total_count, current_page, '/classes.html',5)
        pager = obj.pager_str()

        cls_list = models.Classes.objects.all()[obj.db_start:obj.db_end]

        '''
        # 1, 0,10
        # 2, 10,20
        # 3, 20,30
        start = (current_page - 1) * 10
        end = current_page * 10
        cls_list = models.Classes.objects.all()[start:end]

        total_count = models.Classes.objects.all().count()
        # 99
        # 每页显示10条数据
        # total_count
        v,a = divmod(total_count,10)
        if a != 0:
            v += 1
        pager_list = []
        pager_list.append('<a href="/classes.html?p=%s">上一页</a>' % (current_page-1, ))

        for i in range(1,v+1):
            if i == current_page:
                pager_list.append('<a class="active" href="/classes.html?p=%s">%s</a>'% (i, i,))
            else:
                pager_list.append('<a href="/classes.html?p=%s">%s</a>' %(i,i,))
        pager_list.append('<a href="/classes.html?p=%s">下一页</a>' % (current_page + 1,))

        pager = "".join(pager_list)
        
        '''
        return render(request,'classes.html',{'username': current_user, 'cls_list': cls_list, 'str_pager': pager})

    elif request.method == "POST":
        import json
        response_dict = {'status':True,'error':None,'data':None}

        caption = request.POST.get('caption',None)
        if caption:
            obj = models.Classes.objects.create(caption = caption)
            response_dict['data']={
                'id':obj.id,
                'caption':obj.caption,
            }
        else:
            response_dict['status'] =  False
            response_dict['error'] = '标题不能为空'
        return HttpResponse(json.dumps(response_dict))

@auth
def handle_add_classes(request):
    message = ""
    if request.method == "GET":
        return render(request, 'add_classes.html',{'msg':message})
    elif request.method == "POST":
        caption = request.POST.get('caption',None)
        if caption:
            models.Classes.objects.create(caption = caption)
        else:
            message = "标题不能为空"
            return render(request, 'add_classes.html',{'msg':message})
        return redirect('/classes.html')
    else:
        return redirect('/index.html')
@auth
def handle_edit_classes(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request, 'edit_classes.html',{'obj':obj})
    elif request.method == "POST":
        nid = request.POST.get('nid')
        caption = request.POST.get('caption')
        models.Classes.objects.filter(id=nid).update(caption=caption)
        return redirect('/classes.html')
    else:
        return redirect('/index.html')


def handle_student(request):
    is_login = request.session.get('is_login')
    if is_login:
        current_user = request.session.get('username')
        return render(request,'student.html',{'username':current_user})
    else:
        return redirect('/login.html')

@auth
def add_student(request):
    if request.method == 'GET':
        cls_list = models.Classes.objects.all()[0: 20]
        return render(request,'add_student.html',{'cls_list':cls_list})
    elif request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        cls_id = request.POST.get('cls_id')
        models.Student.objects.create(name=name,email=email,cls_id=cls_id)
        return redirect('/student.html')
@auth
def edit_student(request):
    if request.method == "GET":
        cls_list = models.Classes.objects.all()[0: 20]
        nid = request.GET.get('nid')
        obj = models.Student.objects.get(id=nid)
        return render(request, 'edit_student.html', {'cls_list': cls_list, "obj": obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        cls_id = request.POST.get('cls_id')
        models.Student.objects.filter(id=nid).update(name=name,email=email,cls_id=cls_id)
        return redirect('/student.html')

def handle_teacher(request):
    is_login = request.session.get('is_login')
    if is_login:
        current_user = request.session.get('username')
        return render(request,'teacher.html',{'username':current_user})
    else:
        return redirect('/login.html')

def page(request):
    return render(request,'page.html')

def menu(request):
    # for i in range(10):
    #     models.Province.objects.create(name="河北"+str(i))
    # for i in range(5):
    #     models.City.objects.create(name="廊坊" + str(i),pro_id=1)
    # return HttpResponse("OK")
    pro_list = models.Province.objects.all()
    return render(request,'menus.html',{"pro_list":pro_list})

def fetch_city(request):
    # 根据用户传入的省份ID，获取与其相关的所有市ID
    # ret = {'status': True, 'error': None, 'data': None}
    province_id = request.GET.get('province_id')
    # result = models.City.objects.filter(pro_id=province_id)
    # # QuerySet内部放置对象
    # from django.core import serializers
    # data = serializers.serialize("json", result)
    result = models.City.objects.filter(pro_id=province_id).values('id', 'name')
    # QuerySet内部放置对象
    result = list(result)
    import json
    data = json.dumps(result)
    # result = models.City.objects.filter(pro_id=province_id).values_list('id','name')
    # # QuerySet内部放置对象
    # print(result)
    # result = list(result)
    # import json
    # data = json.dumps(result)

    return HttpResponse(data)

def fetch_xian(request):
    # for i in range(10):
    #     models.Xian.objects.create(name='县'+ str(i), cy_id=1)
    city_id = request.GET.get('city_id')
    xian_list = models.Xian.objects.filter(cy_id=city_id).values('id','name')
    xian_list = list(xian_list)
    return HttpResponse(json.dumps(xian_list))