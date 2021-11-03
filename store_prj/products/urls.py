from django.urls import path
from .views import *
from .models import Clothing
from . import views

app_name = "products"
urlpatterns = [
    path('', home, name= "home"),
    path('search_results/', views.product_list, name='product-list'),
    path('<int:id>', detail, name='detail'),
]