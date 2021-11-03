from django.shortcuts import render, redirect
from .models import Cart, CartItem
from products.models import Clothing
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    product = Clothing.objects.get(id=id)

    cart_item, item_created = CartItem.objects.get_or_create(product_id=product.id, cart_id=cart.id)
    if item_created:
        cart_item.quantity = 1
    else:
        cart_item.quantity += 1
    cart_item.save()
    return redirect("products:home")


@login_required(login_url="/accounts/login")
def get_cart(request):
    cart = Cart.objects.get(user=request.user)
    cartitem = CartItem.objects.filter(cart=cart)
    context = {
        'cartitem' : cartitem
        }
    return render(request, 'cart.html',context)


@login_required(login_url="/accounts/login")
def cart_remove(request, id):
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    product = Clothing.objects.get(id=id)
    try:
        cart_item = CartItem.objects.get(product_id=product.id, cart_id=cart.id)
        if cart_item.quantity > 0 :
            cart_item.quantity -= 1
            cart_item.save()
        else:
            pass
    except:
        pass

    return redirect("products:home")





