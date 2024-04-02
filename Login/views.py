from django.shortcuts import render
import django.contrib.auth.views
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group



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
        group = Group.objects.get(name='Surveyor')
        group.user_set.add(user)
        return redirect('/surveyorlogin')
    else:
        return render(request, 'NewLogin.html')

def takerlogin(request):
    #we need to use something like post.contain because the whole post is a lot more than just the username and password
    if request.method == 'POST':
        if 'proceed_without_login' in request.POST:
            return redirect('/survey/user_surveys')
        username = request.POST['username']
        password = request.POST['password']

        print(request.POST)  # Print the POST data
        user = (request.POST)
        user = authenticate(request, username=username, password=password)
        
        print(user)
        print(status)
        if user is not None:
            django.contrib.auth.login(request, user)
            print(request.user.is_authenticated)  
            return redirect('/user_surveys')
        else:
            message = 'Username or password is incorrect'
            return render(request, 'TakerLogin.html', {'message': message})
    else:
        return render(request, 'TakerLogin.html')
    
def takerregister(request):
    #it is grabbing the GET not the POST, 
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        print(user)
        group = Group.objects.get(name='SurveyTaker')
        group.user_set.add(user)
        return redirect('/takerlogin')
    else:
        return render(request, 'TakerRegister.html')
    
def choose(request):
    return render(request, 'Choose.html')






