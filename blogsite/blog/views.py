#coding=utf-8
from django.shortcuts import render
from blog.models import Article


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
    context['blog']=Article.objects.order_by("-id")
    return render(request,'talkfree.html',context)
