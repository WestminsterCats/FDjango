from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def blist(request):
    return HttpResponse("<h1>blist Page</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('', home),
]
