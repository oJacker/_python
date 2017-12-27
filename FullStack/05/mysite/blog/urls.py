from django.contrib import admin
from django.urls import path,re_path,include

from blog import  views

urlpatterns=[
    path('new/story',views.introduce),
    path('new/login',views.login),
]