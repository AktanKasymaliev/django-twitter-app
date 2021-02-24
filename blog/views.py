from .models import Post, PostImage
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


def posts_list(requests, pk):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, '', {'posts': posts})

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
    return render(request, '', {'form': form})

def post_delete(request, pk):
    pass
