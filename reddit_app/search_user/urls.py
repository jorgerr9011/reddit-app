from django.urls import path
from . import views

urlpatterns = [
    path('reddit_info/', views.user_info, name='reddit_info'),
    path('reddit-form/', views.formulario, name='reddit_form'),
    path('tabla_usuarios/', views.tabla_usuarios, name='tabla_usuarios'),
    path('eliminar_tabla/', views.eliminar_tabla, name='eliminar_tabla'),
    path('subir_tabla/', views.subir_tabla, name='subir_tabla'),
]


