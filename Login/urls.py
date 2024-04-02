# Description: This file contains the URL patterns for the Login app
from django.urls import path
from Login import views
import django.contrib.auth.urls

urlpatterns = [
   
    path('', views.choose, name='choose'),
    path('surveyorlogin/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('takerlogin/', views.takerlogin, name='takerlogin'),
    path('takerregister/', views.takerregister, name='takerregister'),
]