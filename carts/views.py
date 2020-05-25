from django.shortcuts import render, redirect

from productapp.models import Product
from .models import Cart

# Create your views here.
# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print('New Cart Created')
#     return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    return render(request, 'carts/home.html', {})

def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)

    return redirect('cart:home')
