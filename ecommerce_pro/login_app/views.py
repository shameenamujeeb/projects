from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def login(request):

    return render(request, 'login.html')
def registration(request):
    return render(request, 'registration.html')



# Create your views here.
