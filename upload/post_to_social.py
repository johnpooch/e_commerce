from twython import Twython
from urllib.request import urlopen
import requests
import facebook
import os
from django.conf import settings

facebook_message = 'Beautiful Hoffner bass guitar in today.'
twitter_message = 'Beautiful Hoffner bass guitar in today.'
product_url = 'http://e-commerce-johnpooch.c9users.io:8080/products/1239/'
image_url = "http://cdn.shopify.com/s/files/1/0081/3152/products/fullsizeoutput_3a9a_grande.jpeg"

def facebook_get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph

def facebook_post_status():
    cfg = {
    "page_id"      : settings.FACEBOOK_PAGE_ID,
    "access_token" : settings.FACEBOOK_ACCESS_TOKEN
    }
    api = facebook_get_api(cfg)
    attachment = {'link': product_url}
    
    status = api.put_wall_post(message = facebook_message, attachment = attachment)

def twitter_post_status():

    twitter = Twython(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET, settings.TWITTER_OAUTH_TOKEN, settings.TWITTER_OAUTH_TOKEN_SECRET)

    f = open('temp.jpg','wb')
    f.write(urlopen(image_url).read())
    f.close()
    imagen = open('temp.jpg', 'rb')
    image_ids = twitter.upload_media(media=imagen)
    
    ## tweet it!
    twitter.update_status(status=twitter_message+'\n'+product_url, media_ids=[image_ids['media_id']])

def post_to_twitter_and_fb():
    facebook_post_status()
    twitter_post_status()