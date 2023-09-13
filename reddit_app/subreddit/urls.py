from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='subreddit'),
    path('delete/', views.eliminar_subr, name='eliminar_subr'),
    path('chart/', views.get_chart, name='get_chart'),
    path('subirDrive/', views.subirDrive, name='subir_drive')
]