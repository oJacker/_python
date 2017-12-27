
from django.contrib import admin
from django.urls import path,include
from apporm import views
urlpatterns = [
    path('data_open', views.data_open),
]
