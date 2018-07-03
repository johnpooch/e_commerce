from django.db import models
from django.utils import timezone

class About(models.Model):

    about_title = models.CharField(max_length=200)
    about_content = models.TextField()
    address_title = models.CharField(max_length=200)
    address_content = models.TextField()
    contact_title = models.CharField(max_length=200)
    contact_content = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self):
        return self.about_title