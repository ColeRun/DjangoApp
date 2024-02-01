

# Create your views here.
#import httpsresponse and render 
from django.shortcuts import render, HttpResponse

# create a view using home.html 
def home(request):
    return render(request, "home.html")
