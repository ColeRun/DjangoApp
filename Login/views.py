from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login(request):
    return render(request, 'LoginPrompt.html')

