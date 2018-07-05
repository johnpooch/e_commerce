from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import EmailMessage, send_mail
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages, auth
from .forms import UploadForm
from products.models import Product
from django.core.files.storage import FileSystemStorage

def upload(request):
    form_class = UploadForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            
            print("form is valid")
            
            product_name = request.POST.get('product_name', '')
            product_manufacturer = request.POST.get('product_manufacturer', '')
            product_year = request.POST.get('product_year', '')
            product_type = request.POST.get('product_type', '')
            product_description = request.POST.get('product_description', '')
            product_price = request.POST.get('product_price', '')
            product_image = request.FILES['product_image']
            product_featured = request.POST.get('product_featured', '')
            
            p = Product(
                name = request.POST.get('product_name', ''),
                manufacturer = request.POST.get('product_manufacturer', '').upper(),
                year = request.POST.get('product_year', ''),
                type =  request.POST.get('product_type', '').upper(),
                description = request.POST.get('product_description', ''),
                price = request.POST.get('product_price', ''),
                image = request.POST.get('product_image', ''),
                featured = request.POST.get('product_featured', '')
                )
                
            print(p.name+'\n'+
                p.manufacturer+'\n'+
                p.year+'\n'+
                p.type+'\n'+
                p.description+'\n'+
                p.price+'\n'+
                p.featured)

            # SAVE MODEL HERE SO THAT IT CAN BE ACCESSED IN SOCIAL_MEDIA VIEW

            return redirect('social_media')

    print("form is not valid")
    return render(request, 'upload/upload.html', {
        'form': form_class,
    })

def social_media(request):
    
    # ACCESS LAST MODEL WHICH SHOULD BE THE GUITAR.
    
    return render(request, 'upload/social_media.html')