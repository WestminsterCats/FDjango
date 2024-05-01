from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'User logged in')
            return redirect('index')
        else:
            if user is None:
                error_message = 'Error logging in user, user does not exist.'
            else:
                error_message = 'Error logging in user, user is not active.'
            return render(request, 'login/login.html', {'error': error_message})
    else:
        return render(request, 'login/login.html', {})
    

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        # Check if passwords match
        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        # Create the user
        user = User.objects.create_user(username=username, password=password, 
                                         first_name=first_name, last_name=last_name, 
                                         email=email)
        user.is_active = False
        user.save()
        
        # Redirect to a success page or login page
        return redirect('login_user')
    else:
        return render(request, 'login/signup.html')



def admin_view(request):
    return HttpResponseRedirect(reverse('admin:index'))