from django.urls import path
from .views import *
from django_filters.views import FilterView

urlpatterns = [
    path('', all_products, name='all_products'),
    path('acoustic', get_acoustic, name='acoustic'),
    path('electric', get_electric, name='electric'),
    path('bass', get_bass, name='bass'),
    path('amps', get_amps, name='amps'),
    path('effects', get_effects, name='effects'),
    path('pickups', get_pickups, name='pickups'),
    path('audio', get_audio, name='audio'),

    # path('search', FilterView.as_view(filterset_class=ProductFilter,
    #     template_name='products/search.html'), name='search'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('<int:pk>/', product_details, name='product_details'),
    
]