from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.http import HttpResponse

@login_required
def index(request):
    user = request.user

    context = {
        'user' : user
    }

    return render(request, 'userdashboard/userdashboard.html',context)

def signout_view(request):
    logout(request) 
    return redirect(reverse_lazy('login_user'))

#to be filled out with the rest of the pages
def equipment(request):
    return redirect(reverse_lazy('equipment/'))

def reservations(request):
    return redirect('/equipment/reservations')