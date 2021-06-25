from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse("Registration Successful")

def login(request, login_id):
    return HttpResponse("Successful!")

def logout(request, login_id):
    return HttpResponse("Logged out")
