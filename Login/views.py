from django.shortcuts import render
import django.contrib.auth.views

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
import django.contrib.auth.models




def login(request):
 #create logic that if register is clicked it will redirect to register page
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return redirect('/survey')
        else:
            message = 'Username or password is incorrect'
            #display the message
            return render(request, 'LoginPrompt.html', {'message': message})
    else:
        return render(request, 'LoginPrompt.html')
            

   

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.models.User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'NewLogin.html')










