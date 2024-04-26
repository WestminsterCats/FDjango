from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in')
            return redirect('home')  # replace 'home' with the name of your home view
        else:
            messages.error(request, 'Error logging in user, please try again.')
            return redirect('login')  # replace 'login' with the name of your login view
    else:   
        return render(request, 'login\main.html', {})