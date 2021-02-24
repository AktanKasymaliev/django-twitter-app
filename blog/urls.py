
from django.urls import path

from .views import *


urlpatterns = [
    path('home/', posts_list, name='posts_list'),
]
>>>>>>> a68f00abb5cd51d2bffbaa8bdd4171ff66bf7bcd
