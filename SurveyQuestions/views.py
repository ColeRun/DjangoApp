from django.shortcuts import render

# Create your views here.
#call survey template one
def index(request):
    return render(request, 'home1.html')