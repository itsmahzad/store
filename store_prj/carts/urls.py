from django.urls import path
from .models import *
from . import views


app_name = "cart"
urlpatterns = [
    path('add/<int:id>', views.cart_add, name='cart-add'),
    path('remove/<int:id>', views.cart_remove, name='cart-remove'),
    path('accounts/user_home/cart', views.get_cart, name='get-cart'),
]