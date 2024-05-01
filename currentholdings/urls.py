from django.urls import path
from . import views

urlpatterns = [
    path('', views.currentholdings, name='currentholdings'),
    # Add your URL patterns here
]