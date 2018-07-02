from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, ProductImage
from django.core.paginator import Paginator

def paginate(request, products):
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return paginator, page, products
    

def all_products(request):
    products = Product.objects.all()
    return render(request, "products/all_products.html", {'products': products})

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_images = ProductImage.objects.filter(product=pk)
    return render(request, "products/product_details.html", {'product': product, 'product_images': product_images,})
    
def get_acoustic(request):
    products = Product.objects.filter(type="ACOUSTIC")
    paginator, page, products = paginate(request, products)
    return render(request, "products/acoustic.html", {'products': products})
    
def get_electric(request):
    products = Product.objects.filter(type="ELECTRIC")
    paginator, page, products = paginate(request, products)
    return render(request, "products/electric.html", {'products': products})
    
def get_bass(request):
    products = Product.objects.filter(type="BASS")
    paginator, page, products = paginate(request, products)
    return render(request, "products/bass.html", {'products': products})
    
def get_amps(request):
    products = Product.objects.filter(type="AMPLIFIER")
    paginator, page, products = paginate(request, products)
    return render(request, "products/amps.html", {'products': products})
    
def get_effects(request):
    products = Product.objects.filter(type="EFFECTS")
    paginator, page, products = paginate(request, products)
    return render(request, "products/effects.html", {'products': products})
    
def get_pickups(request):
    products = Product.objects.filter(type="PICKUP")
    paginator, page, products = paginate(request, products)
    return render(request, "products/pickups.html", {'products': products})
    
def get_audio(request):
    products = Product.objects.filter(type="AUDIO")
    paginator, page, products = paginate(request, products)
    return render(request, "products/audio.html", {'products': products})
    
def add_to_cart(request):
    product_to_add = get_object_or_404(Product, pk=request.POST["product_id"])
    return HttpResponse("You have added " + product_to_add.name + " to cart")
    

