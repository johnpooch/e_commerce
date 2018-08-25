from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import MakePaymentForm, PurchaseForm
from .models import Purchase, PurchaseLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    if request.method=="POST":
        purchase_form = PurchaseForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if purchase_form.is_valid() and payment_form.is_valid():
        
            purchase = purchase_form.save(commit=False)
            purchase.date = timezone.now()
            purchase.save()
            
            cart = request.session.get('cart', {})
            total = 0
            
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                purchase_line_item = PurchaseLineItem(
                    purchase = purchase,
                    product = product, 
                    quantity = quantity
                    )
                purchase_line_item.save()
                
            try: 
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR", 
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Yor card was declined.")
                
            if customer.paid:
                messages.error(request, "You have successfully paid.")
                request.session['cart'] = {}
                return redirect(reverse('confirmation'))
                
            else: 
                messages.error(request, "Unable to take payment")
            
        else: 
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card.")
        
    else: 
        payment_form = MakePaymentForm()
        purchase_form = PurchaseForm()
        
    return render(request, "checkout/checkout.html", { 'purchase_form': purchase_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })
    
def confirmation(request):
    cart = request.session.pop('cart', {})
    billing_details = Purchase.objects.latest('id')
    return render(request, "checkout/confirmation.html", {'billing_details':billing_details})