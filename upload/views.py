from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import EmailMessage, send_mail
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages, auth
from .forms import UploadForm, SocialMediaForm
from .post_to_social import twitter_post_status, facebook_post_status

from products.models import Product
from django.core.files.storage import FileSystemStorage

def upload(request):

    form = UploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('social_media')
            
        # invalid form response?
    return render(request, 'upload/upload.html', {
        'form': form
    })

def social_media(request):

    product = Product.objects.all().order_by('-id')[0]
    form = SocialMediaForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            
            post_to_facebook = request.POST.get('post_to_facebook')
            post_to_twitter = request.POST.get('post_to_twitter')
            
            product_id = request.POST.get('product_id')
            product_url = "http://e-commerce-johnpooch.c9users.io:8080/products/" + product_id
            image_url = "http://e-commerce-johnpooch.c9users.io:8080" + product.image.url
            
            if post_to_facebook:
                facebook_caption = request.POST.get('facebook_caption')
                facebook_post_status(facebook_caption, product_url)

            if post_to_twitter:
                twitter_caption = request.POST.get('twitter_caption')
                twitter_post_status(twitter_caption, image_url, product_url)
            
            return redirect('get_index')

    print("form is not valid")
    return render(request, 'upload/social_media.html', {
        'form': form, 'product': product,
    })
    return render(request, 'upload/social_media.html')