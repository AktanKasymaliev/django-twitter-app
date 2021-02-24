from .models import Post, PostImage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})


def new_posts(request, pk):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'new_posts.html', locals())

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id=None):
    delete_post=Post.objects.get(id=post_id)
    delete_post.delete()
    return HttpResponseRedirect
    
