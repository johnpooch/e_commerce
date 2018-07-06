from django import forms
from products.choices import *
from products.models import Product
from django.utils import timezone
import datetime
from django.forms import TextInput

class UploadForm(forms.Form):
    product_name = forms.CharField(required=True)
    product_manufacturer = forms.ChoiceField(choices=manufacturers, required=True)
    product_year = forms.ChoiceField(choices=year_choices, widget=forms.Select())
    product_type =  forms.ChoiceField(choices=types, widget=forms.Select(), required=True)
    product_description = forms.CharField(required=True, widget=forms.Textarea)
    product_price = forms.DecimalField(max_digits=6, decimal_places=2, widget=forms.NumberInput())
    product_image = forms.ImageField(required=True)
    product_featured = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].label = "Product name:"
        self.fields['product_manufacturer'].label = "Product manufacturer:"
        self.fields['product_year'].label = "Product year:"
        self.fields['product_year'].initial=2018
        self.fields['product_type'].label = "Product type:"
        self.fields['product_type'].initial = "ELECTRIC"
        self.fields['product_description'].label = "Product description:"
        self.fields['product_price'].label = "Product price:"
        self.fields['product_image'].label = "Image:"
        self.fields['product_featured'].label = "Featured product:"
        
        
class SocialMediaForm(forms.Form):
    
    facebook_caption = forms.CharField(required=False, widget=forms.Textarea)
    post_to_facebook = forms.BooleanField(required=False)
    twitter_caption = forms.CharField(required=False, widget=forms.Textarea) # MAX LENGTH
    post_to_twitter = forms.BooleanField(required=False)
    

    def __init__(self, *args, **kwargs):
        super(SocialMediaForm, self).__init__(*args, **kwargs)
        self.fields['facebook_caption'].label = "Facebook caption:"
        self.fields['twitter_caption'].label = "Twitter caption:"
        self.fields['post_to_facebook'].label = "Post to Facebook:"
        self.fields['post_to_twitter'].label = "Post to Twitter:"
        