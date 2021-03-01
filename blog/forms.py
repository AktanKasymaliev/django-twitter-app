from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'tag', 'image')

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Text area'}),
            'tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tag'}) 
        }

class CommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':2, 'placeholder':'Comment area'}),
        max_length=500, label='New comment')
        
    class Meta:
        model = Comment
        fields = ('message',)
