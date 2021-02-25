from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.core.mail import send_mail



def signingup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts_list')
    else:
        form = SignUpForm()
    return render(request,'accounts/signup.html', locals())