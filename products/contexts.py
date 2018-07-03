from .models import Product

def get_featured_products(request):
    featured_products = Product.objects.filter(featured=True)
    return {"featured_products": featured_products}