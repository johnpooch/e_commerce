from django.urls import path

from .views import all_products, product_details, add_to_cart

urlpatterns = [
    path('', all_products, name='all_products'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('<int:pk>/', product_details, name='product_details'),
    
]