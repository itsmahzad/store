from django.db import models
from djmoney.models.fields import MoneyField

class Clothing(models.Model):
    CLOTHING_TYPE_CHOICES = (
        (1, 'shirt'),
        (2, 'dress'),
        (3, 'pants'),
        (4, 'blouse'),
        (5, 'skirt')
    )
    clothing_name = models.CharField(null=True, blank=True, max_length=50)
    clothing_type = models.IntegerField(null=True, blank=True, choices=CLOTHING_TYPE_CHOICES)
    clothing_color = models.CharField(null=True, blank=True, max_length=50)
    description = models.TextField(null=True, blank=True)
    base_price = MoneyField(null=True, blank=True, max_digits=14, decimal_places=2, default_currency='USD')
    discounted_price = MoneyField(null=True, blank=True, max_digits=14, decimal_places=2, default_currency='USD')
    available = models.BooleanField(null=True, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clothing_name
