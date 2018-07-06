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
            
            print("form is valid")
            
            p = Product(
                name = request.POST.get('product_name', ''),
                manufacturer = request.POST.get('product_manufacturer', '').upper(),
                year = request.POST.get('product_year', ''),
                type =  request.POST.get('product_type', '').upper(),
                description = request.POST.get('product_description', ''),
                price = request.POST.get('product_price', ''),
                image = request.FILES['product_image'],
                featured = request.POST.get('product_featured', '')
                )
                
            print(p.name+'\n'+
                p.manufacturer+'\n'+
                p.year+'\n'+
                p.type+'\n'+
                p.description+'\n'+
                p.price+'\n'+
                p.featured)
                
            if p.featured:
                p.featured = True
            else:
                p.featured = False

            p.save()
            
            # for url in gallery_images:
            #     pi = ProductImage(
            #         product = p,
            #         image = url,
            #         )
            #     pi.save()

            return redirect('social_media')

    print("form is not valid")
    return render(request, 'upload/upload.html', {
        'form': form
    })

def social_media(request):

    product = Product.objects.all().order_by('-id')[0]
    form = SocialMediaForm(request.POST)
    
    if request.method == 'POST':

        
        if form.is_valid():
            print("form is valid")
            
            facebook_caption = request.POST.get('facebook_caption')
            twitter_caption = request.POST.get('twitter_caption')
            post_to_facebook = request.POST.get('post_to_facebook')
            post_to_twitter = request.POST.get('post_to_twitter')
            product_id = request.POST.get('product_id')
            
            if post_to_facebook:
                post_to_facebook = True
            else:
                post_to_facebook = False
                
            if post_to_twitter:
                post_to_twitter = True
            else:
                post_to_twitter = False
            
            print(facebook_caption + '\n')
            print(twitter_caption + '\n')
            print(post_to_facebook)
            print(post_to_twitter)
            
            product_url = "http://e-commerce-johnpooch.c9users.io:8080/products/1204/" + product_id
            
            if post_to_twitter:
                twitter_post_status(twitter_caption, product.image.url, product_url)
                
            if post_to_facebook:
                facebook_post_status(facebook_caption, product_url)
            
            return redirect('get_index')

    print("form is not valid")
    return render(request, 'upload/social_media.html', {
        'form': form, 'product': product,
    })
    return render(request, 'upload/social_media.html')