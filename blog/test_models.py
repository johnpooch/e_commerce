from django.test import TestCase
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
# Create your tests here.

class TestPostModel(TestCase):
    
    def test_post_model(self):
        p_date = timezone.now()
        user = User(username='user', email='user@email.com', password="password")
        user.save()
        post=Post(title="Example Article", author=user, content="Example Content", published_date=p_date)
        post.save()
        self.assertEqual(post.title, "Example Article")
        self.assertEqual(post.content, "Example Content")
        self.assertEqual(post.published_date, p_date)
        
    def test_post_as_string(self):
        post=Post(title="News Article")
        self.assertEqual("News Article", str(post))
