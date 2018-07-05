from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Avg
from .choices import manufacturers, types, year_choices



# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=254, default='')
    manufacturer = models.CharField(max_length=50, choices=manufacturers, null=True)
    year = models.IntegerField(choices=year_choices, default=0)
    type =  models.CharField(max_length=10, choices=types, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField(upload_to='images')
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    featured = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
        
    # This is to allow for multiple images 
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')