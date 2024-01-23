from django.urls import path
from playground import views

urlpatterns = [
    path("", views.home, name="home"),
]