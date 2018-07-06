from django import forms
from products.choices import *
from products.models import Product
from django.utils import timezone
import datetime
from django.forms import TextInput

class UploadForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['published_date']

        
        
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
        