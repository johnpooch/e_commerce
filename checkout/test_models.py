from django.test import TestCase
from .models import Purchase, PurchaseLineItem
from django.utils import timezone

# Create your tests here.
class TestCheckoutModels(TestCase):
    
    def test_purchase_model(self):
        current_date=timezone.now()
        purchase = Purchase(full_name="John Doe", phone_number=123456789, country="Ireland", postcode="A12S34", town_or_city="Some town", street_address_1="1 street_address", street_address_2="2 street address", date=current_date)
        purchase.save()
        self.assertEqual(purchase.full_name, "John Doe")
        self.assertEqual(purchase.phone_number, 123456789)
        self.assertEqual(purchase.country, "Ireland")
        self.assertEqual(purchase.postcode, "A12S34")
        self.assertEqual(purchase.town_or_city, "Some town")
        self.assertEqual(purchase.street_address_1, "1 street_address")
        self.assertEqual(purchase.street_address_2, "2 street address")
        
    def test_purchase_model_as_string(self):
        current_date=timezone.now()
        purchase = Purchase(full_name="John Doe", phone_number=123456789, country="Ireland", postcode="A12S34", town_or_city="Some town", street_address_1="1 street_address", street_address_2="2 street address", date=current_date)
        purchase.save()
        self.assertEqual(str(purchase.id)+"-"+str(purchase.date)+"-John Doe", str(purchase))
        