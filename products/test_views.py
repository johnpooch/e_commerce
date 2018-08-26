from django.test import TestCase
from .models import Product

# Create your tests here.
class TestProductsViews(TestCase):
    
    def test_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home/index.html")
        
    def test_get_product_by_type_page(self):
        page = self.client.get("/products/acoustic")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/products_by_type.html")
        
    def test_get_product_detail_page(self):
        product = Product(name = "Gibson Les Paul 2008", manufacturer = "FENDER", year = 2008, type="acoustic", description = "Beautiful guitar", price = 2000.00, image = "image.jpg", featured=True)
        product.save()
        page = self.client.get("/products/{}".format(product.id))
        self.assertEqual(page.status_code, 200)