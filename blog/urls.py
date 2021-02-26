from django.urls import path
from .views import *


urlpatterns = [
    path('home/', posts_list, name='posts_list'),
    path('detail_post/<int:pk>/', post_detail, name='post_detail'),
    path('new_twit/', new_twit, name='new_twit'),
    path('delete_twit/<int:pk>/', delete_twit, name='delete_twit'),
    path('edit/twit/<int:pk>/', edit_twit, name='edit_twit'),
    path('delete/comment/<int:pk>/', comment_delete, name='comment_delete'),
]
