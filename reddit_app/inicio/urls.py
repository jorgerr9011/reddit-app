from django.contrib import admin
from django.urls import include, path
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('not_found/', views.error, name='error'),
    path('login/', LoginView.as_view(template_name='inicio/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout_view'),
    path('register/', views.register, name='register'),
    ]