# views.py
from django.shortcuts import render


def login(request):

    return render(request, 'registration/login.html')


def signup(request):

    return render(request, 'registration/signup.html')

def logout_view(request):

    return render(request, 'logout.html')