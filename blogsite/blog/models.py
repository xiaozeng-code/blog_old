#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
import datetime

from ckeditor.fields import RichTextField

from taggit.managers import TaggableManager
#from taggit_labels.widgets import LabelWidget
# Create your models here.


class UserProfile(models.Model):
    """
        用户信息类
    """
    user=models.ForeignKey(User,unique=True)
    #头像
    avatar=models.ImageField(upload_to='avatar')

    #基本信息
    nickname=models.CharField(max_length=80)
    realname=models.CharField(max_length=80)
    gender=models.IntegerField(default=0)
    birthday=models.DateTimeField(default=datetime.datetime.now())
    birthcity=models.CharField(max_length=80)
    residecity=models.CharField(max_length=80)

    #个人信息
    affectivestatus=models.IntegerField(default=0)
    lookingfor=models.IntegerField(default=0)
    bloodtype=models.IntegerField(default=0)
    site=models.CharField(max_length=80)
    bio=models.CharField(max_length=255)
    interest=models.CharField(max_length=255)
    sightml=models.CharField(max_length=255)
    timeoffset=models.CharField(max_length=80)
   
    #联系方式
    qq=models.CharField(max_length=80)
    msn=models.CharField(max_length=80)
    taobao=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    phone=models.CharField(max_length=80)
    mobile=models.CharField(max_length=80)
    address=models.CharField(max_length=80)
    zipcode=models.CharField(max_length=80)



class Category(models.Model):
    """
        博客文章分类
    """
    name=models.CharField(max_length=80, default=u'未分类', unique=True,
                            verbose_name=u'名称')
    desc=models.CharField(max_length=200,null=True, blank=True,
                            verbose_name=u'描述')
    createtime=models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Category'


class Article(models.Model):
    """
        博客文章
    """
    title=models.CharField(max_length=200,unique=True,verbose_name=u'标题')
#    author = models.ForeignKey(User, verbose_name=u'作者', editable=False)
    category=models.ForeignKey(Category)
#    content=models.TextField(verbose_name=u'内容')
    content = RichTextField(u"内容")
    tags = TaggableManager(blank=True)
#    tags=TagField(required=False, LabelWidget(model=MyTag))
    createtime=models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
#    createtime=models.DateTimeField(verbose_name=u'创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    public = models.BooleanField(default=True, verbose_name=u'是否公开')
    views = models.PositiveIntegerField(verbose_name=u'浏览次数', default=0, editable=False)

    class Meta:
        db_table = 'Article'


    def __unicode__(self):
        return self.title

