from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','image')

class CommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':2, 'placeholder':'Comment area'}),
        max_length=500, label='Новый комментарий')
    class Meta:
        model = Comment
        fields = ('message',)
