from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def navbar(request):
    return render(request, 'homepage/navbar.html')

def login(request):
    return render(request, 'login/login.html')