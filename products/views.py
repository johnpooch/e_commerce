from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, ProductImage

def all_products(request):
    products = Product.objects.all()
    return render(request, "products/all_products.html", {'products': products})

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_images = ProductImage.objects.filter(product=pk)
    return render(request, "products/product_details.html", {'product': product, 'product_images': product_images,})
    
def add_to_cart(request):
    product_to_add = get_object_or_404(Product, pk=request.POST["product_id"])
    return HttpResponse("You have added " + product_to_add.name + " to cart")
    

