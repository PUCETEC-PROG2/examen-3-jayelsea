from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Artista, Album

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'año_lanzamiento', 'genero', 'artista')
