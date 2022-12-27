from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cartCount = 0
    if 'admin' in request.path:
        return {}
    else:
        try: 
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cartCount += 1
        except Cart.DoesNotExist:
            cartCount = 0
    return dict(cartCount=cartCount)