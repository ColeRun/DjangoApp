from django.shortcuts import render
import django.contrib.auth.views
from django.contrib.auth import authenticate, login


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth.models





 #create logic that if register is clicked it will redirect to register page

def login_view(request):
    #we need to use something like post.contain because the whole post is a lot more than just the username and password
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(request.POST)  # Print the POST data
        user = (request.POST)
        #make a variable "status" that checks if the user is authenticated
        status = authenticate(request, username=username, password=password)
        user = authenticate(request, username=username, password=password)
        
        print(user)
        print(status)
        if status is not None:
            django.contrib.auth.login(request, user)
            print(request.user.is_authenticated)  
            return redirect('/survey')
        else:
            message = 'Username or password is incorrect'
            return render(request, 'LoginPrompt.html', {'message': message})
    else:
        return render(request, 'LoginPrompt.html')

def register(request): 
    #it is grabbing the GET not the POST, 
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        print(user)
        return redirect('/login')
    else:
        return render(request, 'NewLogin.html')









