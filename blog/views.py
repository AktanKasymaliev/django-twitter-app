from .models import Post, PostImage
from django.shortcuts import render
from django.http import HttpResponse

def posts_list(requests, pk):
    return HttpResponse('Hello')

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
    pass

def post_delete(request, pk):
    pass