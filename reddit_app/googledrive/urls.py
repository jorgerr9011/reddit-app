from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns=[
	path('subir_archivo/', views.subir_archivo_drive, name='googledrive'),
    path('subr/', views.subir_subreddit, name='subir_subr'),
    path('subir_reddits/', views.subir_Reddits, name='subir_reddits')
]