from .models import Post, PostImage
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post':post
    }
    return render(request, 'blog/post_detail.html', context)

def new_twit(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            twitt = form.save(commit=False)
            twitt.created_by = request.user
            twitt.date_pub = timezone.now()
            twitt.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'blog/new_posts.html', locals())

def edit_twit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST" and request.user == post.created_by:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.date_pub = timezone.now()
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_twit.html', locals())

def delete_twit(request, pk):
    twit = Post.objects.get(id=pk)
    if request.method == 'POST' and request.user == post.created_by:
        try:
            twit.delete()
            return redirect('posts_list')
        except post.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    return render(request, 'blog/delete_twit.html', locals())
    

