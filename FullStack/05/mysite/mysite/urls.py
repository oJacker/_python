"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include

from blog import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curtime/', views.curtime),
    path('userInfo/', views.userInfo),
    #path(正则表达式, views视图函数，参数，别名),
    path('articles/2003/', views.special_case_2017),
    # djando1.x 与 2.x区别  需要正则表
    #path('articles/<int:year>/', views.year_archive),  # 在方法里面需要传递参数year
    re_path('articles/(?P<year>[0-9]{4})/$', views.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    re_path('articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    #path('articles/<int:year>/<int:month>/<slug>/', views.article_detail),
    re_path('articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[^/]+)/', views.article_detail),
    #path('index/',views.index,{'name':'ojacker'})  # 参数
    path('pay/index/',views.index,name='oj'), # 参数
    path('blog/', include('blog.urls'))

]
