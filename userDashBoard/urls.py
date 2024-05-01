from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('browse/', views.page1, name='page1'),
    path('orders/', views.page2, name='page2'),
    path('cart/', views.page3, name='page3'),
    path('upcoming/', views.page4, name='page4'),
    path('current/', views.page5, name='page5'),
]