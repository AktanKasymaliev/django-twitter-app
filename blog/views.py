from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post':post
    }
    return render(request, 'blog/post_detail.html', context)
