from django.urls import path

from .views import *

urlpatterns = [
    path('', get_repair, name='repair'),
]