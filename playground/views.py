

# Create your views here.
#import httpsresponse and render from django.http and django.shortcuts
from django.http import HttpResponse
from django.shortcuts import render


# create a view using home.html 
def home(request):
    return render(request, 'home.html')