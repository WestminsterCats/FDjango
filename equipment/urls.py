#
# Import
#

from django.urls import path
from . import views

#
# URL patterns
#

urlpatterns = [
    path('', views.equipment, name='equipment'),
    path('reservations/', views.reservations),
    path("item/<str:id>", views.item, name="itempage"),
    path('reserve/', views.reserve_item, name='reserve_item'),
    path('import-items/', views.import_items_view, name='import_items'),
]