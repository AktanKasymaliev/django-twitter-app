from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    date_pub = models.DateField(auto_now_add=True)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='create_posts')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # - генерация уролов для сопостовления дополнительных элементов в урле urls.py
        return reverse('post_detail', kwargs={'pk':self.id})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                            related_name='images')
    image = models.ImageField(upload_to='posts')

