from django.shortcuts import render,HttpResponse
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