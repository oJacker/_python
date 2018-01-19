from django.shortcuts import render,HttpResponse
from app01 import  tasks
# Create your views here.

from celery.result import AsyncResult

import time

def index(request):
    res = tasks.add.delay(5,999)
    print('res:',res)
    return HttpResponse(res.task_id)

def task_res(request):
    pass
