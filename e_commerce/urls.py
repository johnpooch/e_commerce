"""e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from home import urls as home_urls
from products import urls as products_urls
from blog import urls as blog_urls
from about import urls as about_urls
from contact import urls as contact_urls
from upload import urls as upload_urls
from repair import urls as repair_urls
from accounts import urls as accounts_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls

from django.views.static import serve
from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include(home_urls)),
    path('admin/', admin.site.urls),
    path('products/', include(products_urls)),
    path('blog/', include(blog_urls)),
    path('about/', include(about_urls)),
    path('contact/', include(contact_urls)),
    path('upload/', include(upload_urls)),
    path('repair/', include(repair_urls)),
    path('accounts/', include(accounts_urls)),
    path('cart/', include(cart_urls)), 
    path('checkout/', include(checkout_urls)), 
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
