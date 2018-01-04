"""guest URL Configuration

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
from sign import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),  # 添加index/路径配置
    path('login_action/', views.login_action),  # login_action/路径配置
    path('event_manage/', views.event_manage),  # event_manage/路径配置
    path('search_name/', views.search_name),  # search_name/路径配置
    path('guest_manage/', views.guest_manage),  # guest_manage/路径配置
    path('logout/', views.logout),  # guest_manage/路径配置
    re_path('sign_index/(?P<event_id>[0-9]+)/', views.sign_index),  # sign_index/路径配置
    re_path('sign_index_action/(?P<event_id>[0-9]+)/', views.sign_index_action),  # sign_index/路径配置
    path('api/', include('sign.urls',namespace="sign")),
]

