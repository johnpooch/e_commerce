from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import Product, ProductImage
from django.core.paginator import Paginator

def paginate(request, products):
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return paginator, page, products
    
def search(request, products):
    query = request.GET.get("searchquery")
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(year__icontains=query)
            ).distinct() # avoids duplicate items
    query = request.GET.get("brandquery")
    if query:
        products = products.filter(
            Q(manufacturer=query)
            )
    else:
        products = products.order_by('-published_date')
            
    query = request.GET.get("sortquery")
    
    if query == "1":
        products = products.order_by('name')
    
    # A-Z
    elif query == "1":
        products = products.order_by('name')
        
    # Z-A
    elif query == "2":
        products = products.order_by('-name')
    
    # newest to oldest
    elif query == "3":
        products = products.filter(~Q(year=0)).order_by('-year')
        
    # oldest to newest
    elif query == "4":
        products = products.filter(~Q(year=0)).order_by('year')
        
    # Price (high to low)
    elif query == "5":
        products = products.order_by('-price')
        
    # Price (low to high)
    elif query == "6":
        products = products.order_by('price')
        
    return products

def filter_by_brand(request, products):
    return products
def sort_products(request, products):
    return products
    
def get_products_by_type(request, type):
    products = Product.objects.filter(type=type.upper()).order_by('published_date')
    brands = Product.objects.filter(type=type.upper()).order_by().values('manufacturer').distinct()
    products = search(request, products)
    brandquery = request.GET.get("brandquery")
    paginator, page, products = paginate(request, products)
    return render(request, "products/products_by_type.html", {'products': products, "brands": brands, "type": type.title(), "brandquery": brandquery})
    
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_images = ProductImage.objects.filter(product=pk)
    num_images = len(product_images)
    return render(request, "products/product_details.html", {'product': product, 'product_images': product_images, 'range': range(num_images)})
    
def add_to_cart(request):
    product_to_add = get_object_or_404(Product, pk=request.POST["product_id"])
    return HttpResponse("You have added " + product_to_add.name + " to cart")
    

