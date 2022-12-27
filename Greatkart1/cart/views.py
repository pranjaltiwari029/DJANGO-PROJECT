from http.client import HTTPResponse
from multiprocessing import current_process
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart 

# plus button 
def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)

    if current_user.is_authenticated:
        if request.method == "POST":
            for item in request.POST:
                key = item
                value = request.POST[key]

                product_variation = []
                try:
                    variations = Variation.objects.get(id=product_id, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variations)
                except:
                    pass 

        is_cart_item_exists = CartItem.objects.filter(product=product).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product)
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variations = item.variations.all()
                ex_var_list.append(list(existing_variations))
                
            
            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                item = CartItem.objects.create(product=product, quantity=1)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            cart_item = CartItem.objects.create(
                product = product, 
                quantity = 1,
            )
            if(len(product_variation) > 0):
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('cart')   
    else:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                product_variation = []
                try:
                    variations = Variation.objects.get(id=product_id, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variations)
                except:
                    pass 
        

# minus button 
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, totalPrice=0, totalQuantity=0, cart_items=None):
    try:
        tax = 0
        grandTotal = 0
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            totalPrice += (cart_item.product.price * cart_item.quantity)
            totalQuantity += cart_item.quantity
        tax = (10 * totalPrice) / 100
        grandTotal = totalPrice + tax 
    except ObjectDoesNotExist:
        pass 

    data = {
        'totalPrice' : totalPrice,
        'totalQuantity' : totalQuantity,
        'cart_items' : cart_items,
        'tax' : tax,
        'grandTotal' : grandTotal
    }

    return render(request, 'store/cart.html', data)