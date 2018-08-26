from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestUploadViews(TestCase):
    
    def test_cannot_access_upload_if_not_superuser(self):
        page = self.client.get("/upload/")
        self.assertEqual(page.status_code, 302)
        
class TestSocialViews(TestCase):
    
    def test_cannot_access_social_if_not_superuser(self):
        page = self.client.get("/upload/social_media/")
        self.assertEqual(page.status_code, 404)
        
# Can't work out how to test if you can access these pages as superuser