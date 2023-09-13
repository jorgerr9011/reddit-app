from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='index'),
	path('<int:product_id>/',views.detail,name='detail'),
	path('logout/', views.logout_view, name='logout_view'),
	path('signup/', views.signup_view, name='signup_view'),
]
