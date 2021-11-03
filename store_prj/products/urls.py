from django.urls import path
from .views import *
from .models import Clothing
from . import views

app_name = "products"
urlpatterns = [
    path('', home, name= "home"),
    path('<int:id>', detail, name='detail'),
]