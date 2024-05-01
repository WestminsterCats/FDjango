from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('signup/', views.signup_view, name='signup'),
    path('admin/', views.admin_view, name='admin')
    #path("userDashBoard/", include("userDashBoard.urls")),
]