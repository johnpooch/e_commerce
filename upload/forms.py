from django import forms
from products.choices import *
from products.models import Product, ProductImage
from django.utils import timezone
import datetime
from django.forms import TextInput
from django.forms import modelformset_factory

class UploadForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['published_date']
        
class ImagesForm(forms.ModelForm):
    image = forms.ImageField(label='')
    class Meta:
        model = ProductImage
        fields = ['image']
        label = ''
        widgets={
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Upload gallery image here'
                }
            )
        }
        
ImageFormset = modelformset_factory(
    ProductImage,
    fields=('image', ),
    labels = '',
    extra=1,
    widgets={
        'image': forms.FileInput(attrs={
            'class': 'form-control',
            'placeholder': 'Upload gallery image here'
            }
        )
    },
)
        
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
        