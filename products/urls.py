from django.urls import path
from .views import *
from django_filters.views import FilterView

urlpatterns = [
    path('<type>', get_products_by_type, name='products_by_type'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('<int:pk>/', product_details, name='product_details'),
]