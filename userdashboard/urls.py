from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('equipment/', views.equipment, name='equipment'),
    path('reservations/', views.reservations, name='reservations'),
    path('cart/', views.page3, name='page3'),
    path('upcoming/', views.page4, name='page4'),
    path('current/', views.page5, name='page5'),
]