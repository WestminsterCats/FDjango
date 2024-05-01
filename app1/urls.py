#
# Import
#

from django.urls import path
from . import views

#
# URL patterns
#

urlpatterns = [
    path('', views.home, name="Home Page"),
    path('equipment/', views.equipment, name='equipment'),
    path('reservations/', views.reservations),
    path("item/<str:id>", views.item, name="itempage"),
    path('reserve/', views.reserve_item, name='reserve_item'),
]