from django.shortcuts import render
from django.urls.conf import path
from .models import *
from django.http import HttpResponse, JsonResponse
from .filters import ProductFilter


# Create your views here.
def detail(request, id):
    product_obj = Clothing.objects.get(id=id)
    context = {
        "product": product_obj
    }
    return render(request, 'detail.html', context)
    

def home(request):

    product_filter = ProductFilter()
    context = {
        "products": Clothing.objects.all(),
        'product_filter': product_filter
    }
    return render(request, 'home.html', context)

def product_detail(request):
    return render(request, '')


