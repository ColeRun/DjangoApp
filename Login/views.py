from django.shortcuts import render
import django.contrib.auth.views

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect

def login(request):
 #create logic that if register is clicked it will redirect to register page
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return redirect('survey')
        else:
            
            return render(request, 'LoginPrompt.html')
            

    return render(request, 'LoginPrompt.html')

def register(request):
    return render(request, 'NewLogin.html')










