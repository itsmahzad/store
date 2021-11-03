from .models import Clothing
from rest_framework import serializers

class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['clothing_name', 'clothing_type', 'base_price', 'discounted_price']