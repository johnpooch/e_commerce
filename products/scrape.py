import bs4 as bs
from urllib.request import urlopen
import string

from .models import Product, ProductImage

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
        anchors = cut_off.find_all_previous("a", class_="product-img-wrapper")
        
        for anchor in reversed(anchors):
            urls.append(("https://www.someneckguitars.com" + anchor['href'], type))
            
        current_page = current_page + 1
    
    return urls
        

def scrape_product_from_url(url_tuple):
    
    url, type = url_tuple
    regex = r"\b(18|19|20)\d{2}\b"
    
    # default values
    product_year = 0
    product_description = "No description available"
    
    sauce = urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    
    title = soup.find("meta",  property="og:title")
    product_name = title['content']
    
    image = soup.find("meta",  property="og:image")
    product_main_image = image['content']
    
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
        image = product_main_image,
        )
    p.save()
    
    for url in gallery_images:
        pi = ProductImage(
            product = p,
            image = url,
            )
        pi.save()
    

    
def get_products_from_someneck(): 
    product_urls = []
    product_details_list = []
    type_set = set()
    manufacturer_set = set()
    
    print("\n\nscraping data from https://www.someneckguitars.com\n----------------------------------------------- \n")
    
    for type, url in collection_urls.items(): 
        product_urls.extend(scrape_urls_from_collection_page(url, type))
        
    for url_tuple in product_urls:
        
        print('\n' + url_tuple[0].rsplit('/', 1)[-1].replace('-', ' ').title())
        product_details = scrape_product_from_url(url_tuple)
        product_details_list.append(product_details)
        
    
    
    
    
# def get_manufacturer_and_type_from_someneck(): 
#     product_urls = []
#     product_details_list = []
#     type_set = set()
#     manufacturer_set = set()

#     for type, url in collection_urls.items(): 
#         product_urls.extend(scrape_urls_from_collection_page(url, type))
        
#     for url_tuple in product_urls:
        
#         print('\n' + url_tuple[0].rsplit('/', 1)[-1].replace('-', ' ').title())
#         product_details = scrape_product_from_url(url_tuple)
        
#         type_set.add("('" + product_details['type'].upper() + ", '" + product_details['type'].title() + "')")
#         manufacturer_set.add("('" + product_details['manufacturer'].upper() + ", '" + product_details['manufacturer'].title() + "')")
        
#     type_set_list = list(type_set)
#     for i in range(len(type_set_list)):
#         print('\n' + type_set_list[i])
        
#     print ("\n\n=================================\n\n")
        
#     manufacturer_set_list = list(manufacturer_set)
#     for i in range(len(manufacturer_set_list)):
#         print('\n' + manufacturer_set_list[i])
    
 
    
    
# def get_acoustics_from_someneck(): 
#     product_urls = []
#     product_details_list = []
    
#     print("\n\nscraping data from https://www.someneckguitars.com\n----------------------------------------------- \n")
    
#     url = collection_urls["acoustic"]
    
#     product_urls.extend(scrape_urls_from_collection_page(url, 'acoustic'))
        
#     for url_tuple in product_urls[:10]:
        
#         print('\n' + url_tuple[0].rsplit('/', 1)[-1].replace('-', ' ').title())
#         product_details = scrape_product_from_url(url_tuple)
#         product_details_list.append(product_details)

#     print("\nAll products successfully scraped!\n")   

#     return product_details_list
    
    
# def get_single_product_from_someneck():
#     product_urls = []
#     product_details_list = []
    
#     print("\n\nscraping data from https://www.someneckguitars.com\n----------------------------------------------- \n")
    
#     url = collection_urls["acoustic"]
    
#     product_urls.extend(scrape_urls_from_collection_page(url, 'acoustic'))
        
#     for url_tuple in product_urls[:1]:
        
#         print('\n' + url_tuple[0].rsplit('/', 1)[-1].replace('-', ' ').title())
#         product_details = scrape_product_from_url(url_tuple)
#         product_details_list.append(product_details)
        
        
        


#     print("\nAll products successfully scraped!\n")   

#     return product_details_list