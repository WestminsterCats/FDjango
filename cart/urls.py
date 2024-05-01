from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('orders/', views.orders, name='orders')
]