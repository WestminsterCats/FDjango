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

    return render(request, 'userDashBoard.html',context)

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login/'))

#to be filled out with the rest of the pages
def page1(request):
    return render(request, 'userDashBoard.html')

def page2(request):
    return render(request, 'your_app_name/page2.html')

def page3(request):
    return render(request, 'your_app_name/page3.html')

def page4(request):
    return render(request, 'your_app_name/page4.html')

def page5(request):
    return render(request, 'your_app_name/page5.html')
