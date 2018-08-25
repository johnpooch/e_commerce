from django.shortcuts import get_object_or_404
from .models import Post

def news_items(request):
    
    """Ensures that news items are available when rendering every page """
    
    news_items = Post.objects.all().order_by('-published_date')[:3]
    
        
    return { 'news_items': news_items }