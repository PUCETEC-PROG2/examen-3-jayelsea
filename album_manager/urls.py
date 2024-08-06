# Ingresar tus URLs de la app aquí
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('artistas/', views.artista_list, name='artista_list'),
    path('artistas/<int:pk>/', views.artista_detail, name='artista_detail'),
    path('artistas/nuevo/', views.artista_create, name='artista_create'),
    path('artistas/<int:pk>/editar/', views.artista_update, name='artista_update'),
    path('artistas/<int:pk>/eliminar/', views.artista_delete, name='artista_delete'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('albums/nuevo/', views.album_create, name='album_create'),
    path('albums/<int:pk>/editar/', views.album_update, name='album_update'),
    path('albums/<int:pk>/eliminar/', views.album_delete, name='album_delete'),
]
