from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='textblob_comments'),
    path('comments/getComment/<str:subreddit>/', views.getComment, name='getComment'),
]