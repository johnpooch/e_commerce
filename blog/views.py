from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

# Create your views here.

def get_blog(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, "blog/blog.html", {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "blog/postdetail.html", {'post': post})