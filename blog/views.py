from .models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .forms import *


def posts_list(request):
    posts = Post.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts':posts,
                                                'page':page})

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    ccc = post.comments.all()
    comments = post.comments.all()
    new_comment = None
    page_comm = request.GET.get('page')
    paginator = Paginator(comments, 4)
    try:
        comments = paginator.page(page_comm)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == "POST":
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            new_comment = form_comment.save(commit=False)
            new_comment.author = request.user
            new_comment.post_comment = post
            new_comment.sent_at = timezone.now
            new_comment.save()
        else:
            raise Exception('Form is not valid')
    else:
        form_comment = CommentForm()
    return render(request, 'blog/post_detail.html', {'page_comm':page_comm,
                                                    'post':post,
                                                    'comments':comments,
                                                    'ccc':ccc,
                                                    'new_comment':new_comment,
                                                    'form_comment':form_comment})

@login_required
def new_twit(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            twitt = form.save(commit=False)
            twitt.created_by = request.user
            twitt.date_pub = timezone.now()
            twitt.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'blog/new_posts.html', locals())


@login_required
def edit_twit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST" and request.user == post.created_by:
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post_e = form.save(commit=False)
            post_e.created_by = request.user
            post_e.date_pub = timezone.now()
            post_e.image = request.FILES['image']
            post_e.save()
            return redirect('posts_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_twit.html', locals())

@login_required
def delete_twit(request, pk):
    twit = Post.objects.get(id=pk)
    if request.method == 'POST' and request.user == twit.created_by:
        try:
            twit.delete()
            return redirect('posts_list')
        except post.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    return render(request, 'blog/delete_twit.html', locals())

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment,id=pk)
    post = get_object_or_404(Post, pk=comment.post_comment.pk)
    if (request.method == "POST" and request.user == post.created_by) or request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    return render(request, 'blog/comment_delete.html', {'comment':comment,
                                                            'post':post,
                                                            'user':request.user})

@login_required
def delete_image(request, pk):
    twit = Post.objects.get(id=pk)
    image = twit.image
    if request.method == "POST" and request.user == post.created_by:
        try:
            twit.objects.get(id=pk).image_jpeg.delete(save=True)
        except post.DoesNotExist:
            return HttpResponseNotFound("<h2>Picture is not found</h2>")
    return render(request, 'blog/delete_image.html', locals())

@login_required
def my_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_twits = Post.objects.filter(user.username==user)
    context = {
        'username':user,
        'user_twits':user_twits
    }
    print(user_twits)
    print()
    print(user)
    return render(request, 'blog/my_profile.html', context)