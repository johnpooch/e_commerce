from django.shortcuts import get_object_or_404
from django.test import TestCase, Client
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.
class TestNewsViews(TestCase):
    
    def test_news(self):
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        
    # Failing? what does 301 mean?
    def test_get_view_post_page(self):
        user = User(username='user', email='user@email.com', password="password")
        user.save()
        post = Post(title="Example article", author=user, content="example content")
        post.save()
        page = self.client.get("/blog/{0}".format(post.id))
        self.assertEqual(page.status_code, 301)
        