from django.contrib import admin
from .models import Post, Comment
from django.forms import ModelForm


admin.site.register(Post)
admin.site.register(Comment)
