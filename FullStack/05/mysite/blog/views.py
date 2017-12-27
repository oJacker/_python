from django.shortcuts import render,HttpResponse,render_to_response,redirect
import  datetime
# Create your views here.
from blog import models


def curtime(req):
    now_time = datetime.datetime.now()
    # return  HttpResponse("<h1>Welcome</h1>"
    return render(req,"curtime.html",{"nowtime":now_time})


def userInfo(req):
    # req.POST:{"username":oajcker,"sex":male}
    if req.method == 'POST':
        u=req.POST.get("username", None)
        s=req.POST.get("sex", None)
        e=req.POST.get("email", None)
        models.UserInfo.objects.create(
            username=u,
            sex = s,
            email = e,
        )
       # user = {"username":username,"sex":sex,"email":email}
    user_list=models.UserInfo.objects.all()
    return render(req, 'index.html',{"userlist":user_list})


def special_case_2017(req):
    return HttpResponse("Welcome 2017")

def year_archive(req,year):
    return HttpResponse(str(year)+"year")

def month_archive(req,year,month):
    return HttpResponse(str(year)+"year"+str(month)+"month")

def article_detail(req,year,month,slug):
    return HttpResponse("ok")

def index(req):
    if req.method == "POST":
        u = req.POST.get("username")
        p = req.POST.get("passwd")
        if u == 'ojacker' and p == "123":
            return HttpResponse("ok")
    #return render(req,"login.html")
    ojacker="welcome"
    #return render_to_response("new.html",{"name":ojacker})  #有坑
    #locals() 本地变量直接使用，对效率不高，
   # return render_to_response("new.html",locals())
    return  redirect("http://www.baidu.com")

def introduce(req):
    return HttpResponse("introduce ok")

def login(req):
    pass