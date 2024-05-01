from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path("userDashBoard/", include("userDashBoard.urls")),
]