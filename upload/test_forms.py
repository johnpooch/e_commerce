from django.test import TestCase
from.forms import UploadForm, ImagesForm, SocialMediaForm

# Create your tests here.

# Upload Form =====================================================================================

class TestUploadForm(TestCase):
    
    def test_cannot_create_upload_with_just_a_name(self):
        form = UploadForm({ "name": "guitar" })
        self.assertFalse(form.is_valid())
        
    # Incorrect Values ----------------------------------------------------------------------------
    
    def test_cannot_give_string_as_price(self):
        form = UploadForm({ "price": "string" })
        self.assertEqual(form.errors['price'], [u'Enter a number.'])
        
    def test_cannot_give_string_as_image(self):
        form = UploadForm({ "image": "string" })
        self.assertEqual(form.errors['image'], [u'This field is required.'])

    # Missing Values ------------------------------------------------------------------------------

    def test_correct_message_for_missing_name(self):
        form = UploadForm({ "name": '' })
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        
    def test_correct_message_for_missing_manufacturer(self):
        form = UploadForm({ "manufacturer": '' })
        self.assertEqual(form.errors['manufacturer'], [u'This field is required.'])
        
    def test_correct_message_for_missing_year(self):
        form = UploadForm({ "year": '' })
        self.assertEqual(form.errors['year'], [u'This field is required.'])
        
    def test_correct_message_for_missing_type(self):
        form = UploadForm({ "type": '' })
        self.assertEqual(form.errors['type'], [u'This field is required.'])
        
    def test_correct_message_for_missing_price(self):
        form = UploadForm({ "price": '' })
        self.assertEqual(form.errors['price'], [u'This field is required.'])
        
    def test_correct_message_for_missing_image(self):
        form = UploadForm({ "image": '' })
        self.assertEqual(form.errors['image'], [u'This field is required.'])
       