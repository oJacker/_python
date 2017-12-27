from django.shortcuts import render,HttpResponse
from apporm import models
# Create your views here.

def data_open(req):

    # 添加对象
    # create one way
    # pub = models.Publish.objects.filter(id=1)
    # authors = models.Author.objects.filter(id__gt=1)
    # models.Book.objects.create(
    #     title = "漂流记",
    #     price = 1,
    #     color = "yellow",
    #     pulisher_id = 1,
    # )
    book = models.Book.objects.filter(id=1)

    return HttpResponse(book)


