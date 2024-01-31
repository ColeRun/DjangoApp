

# Create your views here.
#import httpsresponse and render 
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

