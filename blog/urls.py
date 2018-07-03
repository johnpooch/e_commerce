from django.urls import path

from .views import *

urlpatterns = [
    path('', get_blog, name='blog'),
    path('<int:pk>/', post_detail, name='post_detail'),
]