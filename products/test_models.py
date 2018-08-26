from django.test import TestCase
from .models import Product
import datetime
# Create your tests here.

class TestProductModel(TestCase):
        
    def test_product_model(self):
        product = Product(name = "Gibson Les Paul 2008", manufacturer = "FENDER", year = 2008, type="acoustic", description = "Beautiful guitar", price = 2000.00, image = "image.jpg", featured=True)
        product.save()
        self.assertEqual(product.name, "Gibson Les Paul 2008")    
        self.assertEqual(product.manufacturer, "FENDER")
        self.assertEqual(product.year, 2008)