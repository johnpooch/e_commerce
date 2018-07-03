from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import Product, ProductImage
from django.core.paginator import Paginator
from .filter import ProductFilter

def paginate(request, products):
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return paginator, page, products
    
def search(request, products):
    query = request.GET.get("q")
    if query:
        print(query)
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(year__icontains=query)
            ).distinct() # avoids duplicate items
    return products

def all_products(request):
    products = Product.objects.all()
    products = search(request, products)
    product_filter = ProductFilter(request.GET, queryset = products)
    return render(request, "products/all_products.html", {'products': products, 'filter': product_filter})
    
def get_acoustic(request):
    products = Product.objects.filter(type="ACOUSTIC")
    products = search(request, products)
    paginator, page, products = paginate(request, products)
    return render(request, "products/acoustic.html", {'products': products})
    
def get_electric(request):
    products = Product.objects.filter(type="ELECTRIC")
    products = search(request, products)
    paginator, page, products = paginate(request, products)
    return render(request, "products/electric.html", {'products': products})
    
def get_bass(request):
    products = Product.objects.filter(type="BASS")
    products = search(request, products)
    paginator, page, products = paginate(request, products)
    return render(request, "products/bass.html", {'products': products})
    
def get_amps(request):
    products = Product.objects.filter(type="AMPLIFIER")
    products = search(request, products)
    paginator, page, products = paginate(request, products)
    return render(request, "products/amps.html", {'products': products})
    
def get_effects(request):
    products = Product.objects.filter(type="EFFECTS")
    products = search(request, products)
    paginator, page, products = paginate(request, products)
    return render(request, "products/effects.html", {'products': products})
    
def get_pickups(request):
    products = Product.objects.filter(type="PICKUP")
    products = search(request, products)
    paginator, page, products = paginate(request, products)
    return render(request, "products/pickups.html", {'products': products})
    
def get_audio(request):
    products = Product.objects.filter(type="AUDIO")
    products = search(request, products)
    paginator, page, products = paginate(request, products)
    return render(request, "products/audio.html", {'products': products})
    
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_images = ProductImage.objects.filter(product=pk)
    return render(request, "products/product_details.html", {'product': product, 'product_images': product_images,})
    
def add_to_cart(request):
    product_to_add = get_object_or_404(Product, pk=request.POST["product_id"])
    return HttpResponse("You have added " + product_to_add.name + " to cart")
    

