from django.db import models

# Create your models here.

class Publisher(models.Model):
    # my_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,verbose_name="名称")
    address = models.CharField("地址",max_length=64)
    city = models.CharField("城市",max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    # 打印对象显示需要的内容

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0,'男'),(1,'女'),))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE,)



class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2,default=10)

    class Meta:
        verbose_name = '书本'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "<%s>"%self.title





