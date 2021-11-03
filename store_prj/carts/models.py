from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from products.models import Clothing

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'cart {self.user.username}'


class CartItem(models.Model):
    product = models.ForeignKey(Clothing, on_delete=CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True,)

    def __str__(self):
        return f' {self.cart.user}, {self.cart.id}, {self.product.id}, {self.quantity}'