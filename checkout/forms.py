from django import forms
from .models import Purchase

class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]
    
    credit_card_number = forms.CharField(label='Card Number', required=False)
    cvv = forms.CharField(label="Security Number (CVV)", required=False)
    expiry_month = forms.ChoiceField(label="Expiration Date", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('full_name', 'phone_number', 'street_address_1', 'street_address_2', 'town_or_city', 'postcode',  'country')