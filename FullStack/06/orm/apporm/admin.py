from django.contrib import admin
admin.autodiscover()
from apporm import models
# Register your models here.



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','publication_date')  # 不能显示多对多的，比如authors:
    search_fields = ("title","publisher",)  #__表示出版社关联到名字
    list_filter = ("publisher",)  #过滤
    #list_editable = ('title', 'publisher', 'publication_date')  # 让后台界面上可以直接修改字段值的关键字定义list_editable
    list_per_page = 10  # 让每页显示几条记录的设置
    ordering = ("price",)
    fieldsets = [
        (None, {'fields': ['title']}),
        ('price information', {'fields': ['price', "publisher"], 'classes': ['collapse']}),
    ]
    filter_horizontal = ('authors',)  # 只针对多+对多
    raw_id_fields = ('publisher',)  # 只针对外键的
admin.site.register(models.Author)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Publisher)
