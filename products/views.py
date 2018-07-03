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
    query = request.GET.get("search-query")
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(year__icontains=query)
            ).distinct() # avoids duplicate items
    return products

def filter_by_brand(request, products):
    query = request.GET.get("brand-query")
    if query:
        products = products.filter(
            Q(manufacturer=query)
            )
    return products
    
def sort_products(request, products):
    query = request.GET.get("sort-query")
    
    # newest to oldest
    if query == "1":
        products = products.order_by('-year')
        
    # oldest to newest
    if query == "2":
        products = products.order_by('year')
        
    # A-Z
    if query == "3":
        products = products.order_by('name')
        
    # Z-A
    if query == "4":
        products = products.order_by('-name')
        
    # Price (high to low)
    if query == "5":
        products = products.order_by('-price')
        
    # Price (low to high)
    if query == "6":
        products = products.order_by('price')
        
    return products
    
def get_products_by_type(request, type):
    products = Product.objects.filter(type=type.upper())
    products = sort_products(request, products)
    brands = Product.objects.filter(type=type.upper()).order_by().values('manufacturer').distinct()
    products = search(request, products)
    products = filter_by_brand(request, products)
    paginator, page, products = paginate(request, products)
    return render(request, "products/products_by_type.html", {'products': products, "brands": brands, "type": type.title()})
    
    
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_images = ProductImage.objects.filter(product=pk)
    return render(request, "products/product_details.html", {'product': product, 'product_images': product_images,})
    
def add_to_cart(request):
    product_to_add = get_object_or_404(Product, pk=request.POST["product_id"])
    return HttpResponse("You have added " + product_to_add.name + " to cart")
    

