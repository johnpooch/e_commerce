from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, ProductImage

import bs4 as bs
from urllib.request import urlopen
import string

import re

collection_urls = {
    "acoustic":'https://www.someneckguitars.com/collections/acoustic',
    "electric": 'https://www.someneckguitars.com/collections/electric',
    "bass": 'https://www.someneckguitars.com/collections/bass',
    "amplifier": 'https://www.someneckguitars.com/collections/amplifiers',
    "effects": 'https://www.someneckguitars.com/collections/accessories',
    "pickup": 'https://www.someneckguitars.com/collections/pickups', 
    "audio": 'https://www.someneckguitars.com/collections/audio',
    }
    
def scrape_urls_from_collection_page(url, type):
    
    print("scraping " + url)
    
    sauce = urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    
    spans = soup.findAll("span",  class_="page")
    
    number_of_pages = "1"
    
    last_span = None
    for last_span in spans:  
        pass
    if last_span:
        number_of_pages = last_span.text
    
    # print("number of pages: " + number_of_pages)
    
    
    current_page = 1
    urls = []
    
    for i in range(int(number_of_pages)):
        
        sauce = urlopen(url + "?page=%i" %(current_page)).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        
        cut_off = soup.find("div", class_="pagination")
        anchors = cut_off.find_all_previous("a", class_="product-img-wrapper")
        
        for anchor in reversed(anchors):
            
            urls.append(("https://www.someneckguitars.com" + anchor['href'], type))
            
        current_page = current_page + 1
    
    # print("\n".join(urls))
    
    return urls
        
    # from products.views import scrape_product_from_url
    # scrape_product_from_url('https://www.someneckguitars.com/collections/featured/products/gretsch-6120-nashville-1971')
    
def scrape_product_from_url(url_tuple):
    url, type = url_tuple
    sauce = urlopen(url).read()

    soup = bs.BeautifulSoup(sauce, 'lxml')
    
    title = soup.find("meta",  property="og:title")
    product_name = title['content']
    
    image = soup.find("meta",  property="og:image")
    product_main_image = image['content']
    
    if soup.find("meta",  property="og:description"):
        description = soup.find("meta",  property="og:description")
        product_description = description['content']
    else:
        product_description = "No description available"
    
    regex = r"\b(18|19|20)\d{2}\b"
    
    product_year = 'N/A'
    
    if re.search(regex, product_description):
        product_year = re.search(regex, product_description).group(0) 
    
    brand_header = soup.find("h2",  itemprop="brand")
    product_manufacturer = brand_header.find('a').text

    
    price_amount = soup.find("meta",  property="og:price:amount")
    product_price_amount = price_amount['content']
    
    price_currency = soup.find("meta",  property="og:price:currency")
    product_price_currency = price_currency['content']
    
    gallery_images = []
    
    # gallery_image = soup.find("meta",  property="og:image")
    for elem in soup.findAll("meta", {"property": "og:image"}):
        gallery_images.append(elem["content"])
        
    product = {
        'name': product_name,
        'manufacturer': product_manufacturer,
        'type': type,
        'year': product_year,
        'description': product_description,
        'price': product_price_amount,
        'image': product_main_image,
    }

    return product
    
    print("\n\n ==================================================================== \n")
    
    print("product name: " + product_name)
    print("product main image url: " + product_main_image)
    print("product main description: " + product_description)
    print("product year: " + product_year)
    print('manufacturer: ' + product_manufacturer)
    print("product price_amount: " + product_price_amount)
    print("product price_currency: " + product_price_currency)
    print("number of gallery images: %s" %(len(gallery_images)))
    # print("\n".join(gallery_images))
    
    p = Product
    p.name = product_name
    p.manufacturer = product_manufacturer
    p.year = product_year
    p.description = product_description
    p.price = product_price_amount
    print(p)
    
    # from products.views import get_products_from_someneck
    
def get_products_from_someneck(): 
    product_urls = []
    product_details_list = []
    
    print("\n\nscraping data from https://www.someneckguitars.com\n----------------------------------------------- \n")
    for type, url in collection_urls.items(): 
        product_urls.extend(scrape_urls_from_collection_page(url, type))
        
    for url_tuple in product_urls[:10]:
        
        print('\n' + url_tuple[0])
        product_details = scrape_product_from_url(url_tuple)
        product_details_list.append(product_details)
        
    for product_details in product_details_list:
        print('\n')
        print(product_details)
    
#  scrape_urls_from_collection_page('https://www.someneckguitars.com/collections/acoustic', "acoustic")

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
    


