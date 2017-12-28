from django.shortcuts import render,HttpResponse
from apporm import models
# Create your views here.

def data_open(req):

    # 添加对象
    # create one way
    # pub = models.Publish.objects.filter(id=1)
    # authors = models.Author.objects.filter(id__gt=1)
    # models.Book.objects.create(
    #     title = "php",
    #     publisher_id = 2,
    #     publication_date='2017-12-28',
    #     price = 99,
    # )
    # models.Publisher.objects.create(name='河大出版社',address='保定',city='保定',
    #             state_province='河北',country='China',website='http://www.hbu.com')
    book = models.Book.objects.filter(id=1)
    pub_obj = models.Publisher.objects.get(id=1)
    return HttpResponse(pub_obj)


    '''
    #多对多(ManyToManyField()):

    author1=models.Author.objects.get(id=1)
    author2=models..Author.objects.filter(name='alvin')[0]
    book=models.Book.objects.get(id=1)
    models.book.authors.add(author1,author2)
    #等同于:
    models.book.authors.add(*[author1,author2])
    models.book.authors.remove(*[author1,author2])
    #-------------------
    book=models.Book.objects.filter(id__gt=1)
    authors=models.Author.objects.filter(id=1)[0]
    models.authors.book_set.add(*book)
    models.authors.book_set.remove(*book)
    #-------------------
    models.book.authors.add(1)
    models.book.authors.remove(1)
    models.authors.book_set.add(1)
    models.authors.book_set.remove(1)
    '''