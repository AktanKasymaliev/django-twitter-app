from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog/index.html', context)


