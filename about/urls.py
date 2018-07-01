from django.urls import path

from .views import *

urlpatterns = [
    path('', get_about, name='about'),
]