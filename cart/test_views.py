from django.test import TestCase
from decimal import Decimal

# Create your tests here.
class TestCartViews(TestCase):
    
    def test_view_cart(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart/cart.html")
        