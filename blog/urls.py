
from django.urls import path

from .views import *


urlpatterns = [
    path('home/', posts_list, name='posts_list'),
]
