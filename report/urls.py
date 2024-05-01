from django.urls import path
from . import views

urlpatterns = [
    path('', views.report, name='report'),
    path('download/', views.download, name='download'),
]