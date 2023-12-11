# views.py
from django.shortcuts import render


def login(request):
    # Your login logic goes here
    return render(request, 'registration/login.html')


def signup(request):
    # Your sign-up logic goes here
    return render(request, 'registration/signup.html')
