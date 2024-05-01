from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('equipment/', views.equipment, name='equipment'),
    path('reservations/', views.reservations, name='reservations'),
    path('signout/', views.signout_view, name='signout')
]