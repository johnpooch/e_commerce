[![Build Status](https://travis-ci.org/johnpooch/e_commerce.svg)](https://travis-ci.org/johnpooch/e_commerce)

# E-Commerce Vintage Guitar Shop (Some Neck Guitars)

### About Some Neck Guitars
Some Neck Guitars is a guitar shop in Dublin which specialises in vintage and used guitars. The shop also sells amplifiers, effects pedals, pickups, and audio processing units.

### Motivations Behind the Project
This project is designed to be a redesign of the current Some Neck Guitars website (https://www.someneckguitars.com). The current Some Neck Guitars website was built using Shopify. The design of the website is a little lacklustre and there are a number of features which would be expected from an E-commerce site that are missing. This project represents an improved design for the site and includes a number of features which are not on the original site.

### Project Stack Overview
This project is built using HTML5, CSS, JavaScript (jQuery), Python3, and Django2. The website uses the Django default SQLite3 database for local development. PostgreSQL is used for production development. The site is hosted using Heroku and the media files for the Heroku version are stored using AWS S3. The code is tested using the Django test library. 

The site accesses the Facebook and Twitter APIs to allow the shop owner to post to Facebook and Twitter automatically when uploading a new product. This is done using facebook-sdk 2.0.0 and twython 3.7.0.

The products on the site were scraped directly from the original Some Neck website. This was done using Beautiful Soup 4. Payments are handled using Stripe. The site is mobile-responsive. 

### Live Version
 
This website is not used by Some Neck Guitars. The site was created purely for educational purposes. Please don't give real credentials in the checkout and accounts sections as the site is not fully secure.

Live version: https://e-commerce-johnpooch.herokuapp.com/

## Getting Started

Follow these instructions to run the site locally. 

### Installation

Clone this workspace and install the required software:

```
$ pip3 install -r requirements.txt
```

or if you're using Cloud9:

```
$ sudo pip3 install -r requirements.txt
```

You should now be able to run the site locally. There will be no products on the site.

```
$ python3 manage.py runserver $IP:<PORT>
```

### Running the tests

To carry out the automated tests:

```
$ python3 manage.py test
```

## Scraping from original Some Neck website
A total of 313 products, including prices, descriptions, images, manufacturer, etc., were scraped from the original Some Neck website using Beautiful Soup 4. This functionality is conatined within products/scrape.py and could be run in the django command shell using one function call. The code worked through every page of products on the website and was able to handle pagination. 

Code in action:

<img src="/source/images/Screen Shot 2018-08-25 at 15.12.49.png?raw=true"/>

## Automatic posting to Twitter and Facebook
One of the features in this project is the ability to automatically post a product to Facebook and Twitter when uploading a product. This means that the shop owner can more easily manage the social media of the shop. Dummy Twitter and Facebook accounts were made to demonstrate the feature.

#### Twitter account with no posts - pre-upload:
<img src="/source/images/Screen Shot 2018-08-26 at 11.54.52.png?raw=true"/>

#### Facebook account with no posts - pre-upload:
<img src="/source/images/Screen Shot 2018-08-26 at 11.55.35.png?raw=true"/>

#### Upload form:
<img src="/source/images/Screen Shot 2018-08-26 at 12.02.10 (2).png?raw=true"/>

#### Social media form:
<img src="/source/images/Screen Shot 2018-08-26 at 12.05.17.png?raw=true"/>

#### Twitter after upload:
<img src="/source/images/Screen Shot 2018-08-26 at 12.06.12.png?raw=true"/>

#### Facebook after upload: 
<img src="/source/images/Screen Shot 2018-08-26 at 12.10.18.png?raw=true"/>


## Built With

* [Django](https://www.djangoproject.com/) - The Django web framework.
* [AWS S3](https://console.aws.amazon.com/s3/) - Used to store media for Heroku version. 
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Used to scrape original Some Neck Website.
* [Stripe](https://stripe.com/gb) - Used to handle payments.

## Acknowledgments

* Sentdex's video series on working with Beautiful Soup: https://www.youtube.com/watch?v=aIPqt-OdmS0


