from django.db.models import fields
import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Clothing
        fields = '__all__'
        exclude = ['description', 'created', 'updated', ]