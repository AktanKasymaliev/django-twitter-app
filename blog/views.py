
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def posts_list(requests):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts_list.html', context)


