[![Build Status](https://travis-ci.org/johnpooch/e_commerce.svg)](https://travis-ci.org/johnpooch/e_commerce)

# E-Commerce Vintage Guitar Shop (Some Neck Guitars)

### About Some Neck Guitars
Some Neck Guitars is a guitar shop in Dublin which specialises in vintage and used guitars. The shop also sells amplifiers, effects pedals, pickups, and audio processing units.

### Motivations Behind the Project
This project is designed to be a redesign of the current Some Neck Guitars website (https://www.someneckguitars.com). The current Some Neck Guitars website was built using Shopify. The design of the website is a little lacklustre and there are a number of features which would be expected from an E-commerce site that are missing. This project represents an improved design for the site and includes a number of features which are not on the original site.

### Project Stack Overview
This project is built using HTML5, CSS, JavaScript (jQuery), Python3, and Django2. The website uses the Django default SQLite3 database for local development. PostgreSQL is used for production development. The site is hosted using Heroku and the media files for the Heroku version are stored using AWS S3. The code is tested using the Django test library. 

The site accesses the Facebook and Twitter APIs to allow the shop owner to post to Facebook and Twitter automatically when uploading a new product. This is done using facebook-sdk 2.0.0 and twython 3.7.0.

The products on the site were scraped directly from the original Some Neck website. This was done using Beautiful Soup 4. Payments are handled using Stripe. The site is mobile-responsive. This was done using Bootstrap 4.

### Live Version
 
This website is not used by Some Neck Guitars. The site was created purely for educational purposes. Please don't give real credentials in the checkout and accounts sections as the site is not fully secure.

Live version: http://johnpooch-diplomacy.herokuapp.com/initialise

## Getting Started

Follow these instructions to run the game locally. 

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

![alt text](~/workspace/static/images/screenshots/Screen Shot 2018-08-25 at 15.12.49.png?raw=true)

## Automatic posting to Twitter and Facebook
One of the features in this project is the ability to automatically post a product to Facebook and Twitter when uploading a product. This means that the shop owner can more easily manage the social media of the shop. 

## Apps

#### Home

The Home App renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

#### Accounts

The Accounts App is used for full user authentication. When users first visit the website they have two options under 'My Account' - Register if they have no account or Log In if they do. Once Registered/Logged in they can view their own profile that will display their username and email address they used to register with. The two options under 'My Account will then change to Profile or Log Out. It is possible for users to Subscribe to a monthly magazine - once clicked the subscribe function is called within the views.py in the Accounts App which connects with Stripe payments and if the card details are entered correctly into the form it will take a monthly payment from the user.

#### Products/Categories

These Apps display the Products that have been added via Django's admin panel

#### Search

The Search App uses a simple Python function to search through all the products & render the results.html page which displays them

#### Payments/Cart

The Cart App stores the size, quantity and price of all products selected and disaplays a basket total. The Payments App then renders a form for a one-off Stripe payment.

#### Contact

The Contact App is used when the 'Contact Us' link is clicked. The anchor link's href attribute points to the URL 'contact'. From the top level urls.py the 'contact' function is called from the views.py in the Contacts App. This renders the contact.html page which displays the form which has been defined in forms.py within the Contact App. Once the user fills the form in, the 'contact' function is called which checks if the form is valid. If the form is valid, an automatic email is sent to the user acknowledging reciept of the enquiry and a copy of the enquiry is emailed to the website owner - the user is re-directed back to index.html and a styled Django message appears at the top acknowledging receipt.

#### Blog

blogposts.html displays all blog posts that have been created, either via Django's admin panel or via the form in blogpostform.html. A post consists of a title, content image and tag. The words are truncated to show only 30 words on the main screen so users must click into the blog post to read the entire thing (postdetail.html) Users must be logged in to create or edit posts.
django-disqus must be pip-installed to manage comments on blogposts as well as Pillow, which facilitates upload of images. 

## Issues with the original website

#### Original website has a lacklustre design
The design of the original website is somewhat dull. There are large areas with monochrome and textureless backgrounds. 

A large proportion of the navbar is occupied by a banner showing the number of items in the cart and the total value of the cart items. Because of the value of the products, most users on the site would not be making purchases directly from the site. As such, this banner is unnecessarily large.

###### Solution
Textured backgrounds, borders, shadows, responsiveness, and other stylistic elements were used in this project to bring life to the website. The design of the site is a work in progress. 

#### Original website does not have users/accounts
Returning customers cannot create accounts on the site. This means that users can't save products which they like or comment on products, etc. 

###### Solution
This project has a users and accounts. The functionality of the users/accounts system has not been fully developed.

#### Original website has defunct blog section
While the original website has a blog section, the blog has only one post which was posted in 2015. The shop is regularly visited by internationally renowned musicians. The shop also carry out repairs on rare guitars. If the shop posted to its blog about how to maintain rare guitars or about celebrities visiting the shop, this could result in greater traffic to the website.

###### Solution
This project has a re-designed blog/news section which included more posts and is more appealing to read.

#### Original website does not have a search feature
The original Some Neck Guitars website does not have a search feature. The website has around 400 products on it. As such it can be difficult to determine whether the shop has the specific product you're be looking for. The website has a 'sort by' feature which orders the products, and a 'filter by brand' feature which displays only products of a given manufacturer. A search bar is a more intuitive way of filtering products.

###### Solution
This project features a search bar. The search bar can be used in conjunction with the 'sort by' and 'filter by' features. 

#### 'Sort by' options are not intuitive
On the original site, the 'sort by' options are not intuitive. 

The 'Newest to Oldest' option orders the products by the date at which they were uploaded to the site. Given that the shop specialises in vintage and used guitars, it would make more sense to order the products by the year of manufacturing. This would allow users to look at older guitars or newer guitars.

The 'Best Selling' option is redundant because the products on the site are unique.

###### Solution
In this project, the 'Newest to Oldest' option orders the products by the year of manufacturing. Another option called recently added is included to see products that habve been recently added to the page. The 'Best Selling' feature is removed. 

#### Original website contact and about pages are virtually identical
The 'contact us' and 'about' pages on the original website are almost identical. The only difference between the two pages is that the 'contact us' page features a Google map. This creates the impression of the website being unprofessional. 

###### Solution
This project doesn't have an 'about' page at present. In the future an 'about' page will be added which will be entirely separate from the 'contact us' page.

#### Original website doesn't have a browser image
The original website does not have an image in the browser tab. This is a simple feature to implement which improves the appearance of the site.

###### Solution
In this project the profile image of the Some Neck Facebook page was used as a browser icon.

## Current Issues

The project has a number of issues which could not be resolved because of time constraints.

#### Cluttered navbar
The navbar on the site is a bit cluttered especially on smaller displays. By using collapsable lists, the navbar could be cleaner. 

#### Missing footer section
The page does not have a footer section. This section should feature a mini navbar and contact details. The section could also include links to social media. 

#### Blog to News
Originally, the news section was intended to be a blog. Half way through development it was decided that it would be a news section. This section is called 'blog' and 'news' in the code. This is misleading to other developers. The naming should be standardised.

#### Confirmation page is unfinished
After making a purchase, users are redirected to a confirmation page. This page is unfinished. When the page is finished it should present the user with the product(s) that have just been purchased as well as the billing details of the purchase so that the user can review the details of the purchase.

#### Dark Appearance
The design of the 'product_by_type' pages rely on dark background textures. I feel that this makes the page less appealing to look at and makes the information harder to read. A brighter background texture would imporve these pages.

#### Screen Size issues
On smaller laptops, the navbar section becomes increasingly cluttered. While the site is mobile-responsive, it does not work well with small laptop screens. Media queries should be used to address this.

#### Facebook and Twitter
The feature which posts to Facebook and Twitter only allows for a caption and a link. The shop owner might want to tag other Facebook and Twitter users or might want to include hashtags or emojis. A more fully featured posting system would be useful.

#### Posting old products to Facebook and Twitter
At present, the shop owner can only post new products to Facebook and Twitter. The shop owner might want to post older products to facebook or twitter as well. This should be a feature. 

## Future Development Plans

#### Dynamic Search
A dynamic search feature which presents search results in real time would be a good feature to add. This would probably rely on AJAX. 

#### Messaging system shop
A feature whereby users could contact the shop in real time would be useful. This would also use AJAX. 

#### Accounts features
Users/accounts have very little functionality in the project at present. Features like wish-lists, commenting, recommendations, etc. should be introduced.

## Built With

* [Django](https://www.djangoproject.com/) - The Django web framework.
* [AWS S3](https://console.aws.amazon.com/s3/) - Used to store media for Heroku version. 
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Used to scrape original Some Neck Website.
* [Stripe](https://stripe.com/gb) - Used to handle payments.

## Acknowledgments

* Sentdex's video series on working with Beautiful Soup: https://www.youtube.com/watch?v=aIPqt-OdmS0


