from django.contrib.auth import login
from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout_view'),
   path('edit_profile/', views.edit_profile, name='edit-profile'),
   path('user_home/', views.user_home, name='user-home'),
   
]

