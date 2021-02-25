from django import forms
from .models import Post, PostImage, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
