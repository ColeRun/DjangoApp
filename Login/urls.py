# Description: This file contains the URL patterns for the Login app
from django.urls import path
from Login import views

urlpatterns = [
   
    path('', views.login, name='login'),
]