from django.db import models

# Create your models here.

class Publish(models.Model):
    # my_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=63)

    def __str__(self):
        return self.city

class Author(models.Model):
    name = models.CharField(max_length=30)

    # 打印对象显示需要的内容
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=64)
    page_num = models.IntegerField(null=True)
    pulisher = models.ForeignKey("Publish", on_delete=models.CASCADE,)

    # 接受对象
    author = models.ManyToManyField("Author")
    def __int__(self):
        return self.price

    def __str__(self):
        return self.title+self.color



