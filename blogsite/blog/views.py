#coding=utf-8
from django.shortcuts import render
from blog.models import Article
from django.shortcuts import get_object_or_404

# Create your views here.

# Create your views here.
def home(request):
    """page first"""
    context={}
    context['blog']=Article.objects.order_by("-id")
    return render(request,'index.html',context)

def talkfree(request):
    """详谈生活"""
    context={}
    context['blog']=Article.objects.filter(category__name='闲谈生活').order_by('-id')
    return render(request,'talkfree.html',context)


#根据文章ID查看文章详情
def talkdetail(request,record):
    context={}
    print record
    context['blog']=get_object_or_404(Article,pk=int(record))
    return render(request,'talkdetail.html',context)
