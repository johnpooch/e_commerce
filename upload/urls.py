from django.urls import path

from .views import *
 
urlpatterns = [
    path('', upload, name='upload'),
    path('social_media', social_media, name='social_media'),
]