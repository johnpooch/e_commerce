from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Avg

# Create your models here.
class Product(models.Model):
    
    manufacturers = (
        ('FENDER', 'Fender'),
        ('GIBSON', 'Gibson'),
        ('GRETSCH', 'Gretsch'),
        ('EPIPHONE', 'Epiphone'),
    )
    
    types = (
        ('ELECTRIC', 'Electric'),
        ('ACOUSTIC', 'Acoustic'),
        ('BASS', 'Bass'),
    )
    
    year_choices = []
    for r in range(1800, (datetime.datetime.now().year+1)):
        year_choices.append((r,r))
    
    name = models.CharField(max_length=254, default='')
    manufacturer = models.CharField(max_length=50, choices=manufacturers, null=True)
    year = models.IntegerField(choices=year_choices, default=datetime.datetime.now().year)
    type =  models.CharField(max_length=10, choices=types, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField(upload_to='images')
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.name
        
    # This is to allow for multiple images 
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete='PROTECT')
    image = models.FileField(upload_to='images')