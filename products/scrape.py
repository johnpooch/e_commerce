from django.conf import settings
import bs4 as bs
from urllib.request import urlopen
from urllib import parse
import string

from .models import Product, ProductImage

import requests
import tempfile
from PIL import Image
from django.core import files

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import requests
import os
import boto3



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
    
featured_urls = set()

def save_image_from_url(field, url):

    r = requests.get(url)

    if r.status_code == requests.codes.ok:

        img_temp = NamedTemporaryFile(delete = True)
        img_temp.write(r.content)
        img_temp.flush()

        img_filename = parse.urlsplit(url).path[1:]
        
        print(img_filename)
        
        field.save(img_filename, File(img_temp), save = True)
        
        # FOR UPLOADING TO AWS
        s3 = boto3.resource('s3')
        s3.Bucket('e-commerce-johnpooch').put_object(Key="media/images/" + img_filename, Body=r.content)
        
        # FOR UPLOADING TO LOCAL
        # with open(settings.MEDIA_ROOT + "/images/" + img_filename, "wb") as f:
        #     f.write(r2.content)

        return True

    return False
    
def scrape_urls_from_collection_page(url, type):
    
    number_of_pages = "1"
    current_page = 1
    urls = []
    
    print("scraping " + url)
    sauce = urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    
    spans = soup.findAll("span",  class_="page")
    last_span = None
    for last_span in spans:  
        pass
    if last_span:
        number_of_pages = last_span.text
    
    for i in range(int(number_of_pages)):
        sauce = urlopen(url + "?page=%i" %(current_page)).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        
        cut_off = soup.find("div", class_="pagination")
        non_featured_anchors = cut_off.find_all_previous("a", class_="product-img-wrapper")
        featured_anchors = cut_off.find_all_next("a", class_="product-img-wrapper")
        
        for anchor in reversed(non_featured_anchors):
            urls.append(("https://www.someneckguitars.com" + anchor['href'], type))
          
        for anchor in reversed(featured_anchors):
            featured_urls.add("https://www.someneckguitars.com" + anchor['href'])  
            
        current_page = current_page + 1
    
    return urls
        

def scrape_product_from_url(url_tuple):
    
    url, type = url_tuple
    regex = r"\b(18|19|20)\d{2}\b"
    
    # default values
    product_year = 0
    product_description = "No description available"
    
    if url in featured_urls:
        product_featured = True
        print("featured product found")
    else:
        product_featured = False
    
    sauce = urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    
    title = soup.find("meta",  property="og:title")
    product_name = title['content']
    
    image = soup.find("meta",  property="og:image")
    image_url = image['content']
    
    if soup.find("meta",  property="og:description"):
        description = soup.find("meta",  property="og:description")
        product_description = description['content']
        
    if re.search(regex, product_description):
        product_year = re.search(regex, product_description).group(0) 
    
    brand_header = soup.find("h2",  itemprop="brand")
    product_manufacturer = brand_header.find('a').text

    price_amount = soup.find("meta",  property="og:price:amount")
    product_price_amount = float(price_amount['content'].replace(',',''))
    
    price_currency = soup.find("meta",  property="og:price:currency")
    product_price_currency = price_currency['content']
    
    gallery_images = []
    
    
    for image_element in soup.findAll("meta", {"property": "og:image"}):
        gallery_images.append(image_element["content"])
        
    p = Product(
        name = product_name,
        manufacturer = product_manufacturer.upper(),
        year = product_year,
        type =  type.upper(),
        description = product_description,
        price = product_price_amount,
        # image = product_image,
        featured = product_featured
        )
        
    save_image_from_url(p.image, image_url)
        
    p.save()
    
    for url in gallery_images:
        pi = ProductImage(
            product = p,
            )
        save_image_from_url(pi.image, url)
        pi.save()
    

    
def get_products_from_someneck(): 
    product_urls = []
    product_details_list = []
    type_set = set()
    manufacturer_set = set()
    
    print("\n\nscraping data from https://www.someneckguitars.com\n----------------------------------------------- \n")
    
    for type, url in collection_urls.items(): 
        product_urls.extend(scrape_urls_from_collection_page(url, type))
        
    for url_tuple in product_urls[::-1]:
        
        print('\n' + url_tuple[0].rsplit('/', 1)[-1].replace('-', ' ').title())
        product_details = scrape_product_from_url(url_tuple)
        product_details_list.append(product_details)
