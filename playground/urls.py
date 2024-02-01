from django.urls import path
from playground import views

urlpatterns = [
    #create a path to the home view using home.html
    path('', views.home, name='home'),
]