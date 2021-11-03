from django.urls import path, re_path

from products import views_admin
from .views import *
from .models import Clothing
from . import views

app_name = "products"
urlpatterns = [
    path('', home, name= "home"),
    path('search_results/', views.product_list, name='product-list'),
    path('<int:id>', detail, name='detail'),
    re_path('products_view/(?P<pk>\d+|)', views_admin.ProductsAdminView.as_view(), name='products-admin'),
]