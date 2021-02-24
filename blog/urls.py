from django.urls import path
from .views import *


urlpatterns = [
    path('home/', posts_list, name='posts_list'),
    path('detail_post/<int:pk>', post_detail, name='post_detail')
    path('delete/<post_id>', delete_post, name='delete')
]
