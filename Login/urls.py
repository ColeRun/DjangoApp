# Description: This file contains the URL patterns for the Login app
from django.urls import path
from Login import views
import django.contrib.auth.urls

urlpatterns = [
   
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
]