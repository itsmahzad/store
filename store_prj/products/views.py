from django.shortcuts import render
from .models import *
from .filters import ProductFilter


# Create your views here.
def detail(request, id):
    product_obj = Clothing.objects.get(id=id)
    context = {
        "product": product_obj
    }
    return render(request, 'detail.html', context)
    

def home(request):
    context = {
        "products": Clothing.objects.all()
    }
    return render(request, 'home.html', context)

def product_detail(request):
    return render(request, '')


def product_list(request):
    myfilter = ProductFilter(request.GET, queryset=Clothing.objects.all())
    return render(request, 'product_list.html', {'filter': myfilter})