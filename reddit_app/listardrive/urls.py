from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='listar_drive'),
    path('eliminar_archivo/', views.eliminar_archivo, name='eliminar_archivo'),
    path('eliminar_drive/', views.eliminar_drive, name='eliminar_drive')
]