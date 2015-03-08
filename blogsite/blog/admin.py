#coding=utf-8
from django.contrib import admin
from blog.models import Category,Article


# Register your models here.


admin.site.register([Category,Article]);