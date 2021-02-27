from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor


class Post(models.Model):
    title = models.CharField(max_length=100)
    date_pub = models.DateField(auto_now_add=True)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='create_posts')
    image = fields.ImageField(blank=True, help_text="Minimal reslution for image: 100x100\nMax resolution for image: 1000x1000", upload_to='images', dependencies=[
        FileDependency(attname='image_jpeg', processor=ImageProcessor(
            format='JPEG', scale={'max_width': 600, 'max_height': 600})),
              ])                    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # - генерация уролов для сопостовления дополнительных элементов в урле urls.py
        return reverse('post_detail', kwargs={'pk':self.id})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE,
                                    related_name='comments')
    author = models.CharField(max_length=50)
    message = models.TextField()
    sent_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post_comment}"


    class Meta:
        ordering = ['-sent_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    