from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import  auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
# Create your views here.

def index(request):
    return render(request,'index.html')

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录
            request.session['user'] = username #将session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        # if username == 'admin' and password == 'admin123':
        #     response = HttpResponseRedirect('/event_manage/')
        #     response.set_cookie('user',username,3600)  #添加浏览器cookie
        #     return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})
    else:
        return render(request, 'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')  # 读取浏览器cookie
    return render(request, 'event_manage.html', {'user': username,'events':event_list})

def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username,
                                                 "events": event_list})