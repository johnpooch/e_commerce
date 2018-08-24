from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    
    """ Renders the cart contents page """
    return render(request, "cart/cart.html")
    
    
def add_to_cart(request):
    
    """ Adds a product to the cart """
    id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
def remove_from_cart(request):
    
    """ Adjust quantity of the specified product """
    
    
    cart = request.session.get('cart', {})
    cart.pop(request.POST.get('product_id'))
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))