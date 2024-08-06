
from django.shortcuts import render, get_object_or_404, redirect
from .models import Artista, Album
from django.http import HttpResponse
from .forms import ArtistaForm, AlbumForm
#Inicio
def index(request):
    return render(request, 'index.html')
# Vistas para Artista
def artista_list(request):
    artistas = Artista.objects.all()
    return render(request, 'artista_list.html', {'artistas': artistas})

def artista_detail(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    return render(request, 'artista_detail.html', {'artista': artista})

def artista_create(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo artista en la base de datos
            return redirect('artista_list')  # Redirige a la lista de artistas después de guardar
    else:
        form = ArtistaForm()
    return render(request, 'artista_form.html', {'form': form})

def artista_update(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('artista_list')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'artista_form.html', {'form': form})

def artista_delete(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('artista_list')
    return render(request, 'artista_confirm_delete.html', {'artista': artista})

# Vistas para Album
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form, 'artistas': Artista.objects.all()})

def album_update(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form, 'artistas': Artista.objects.all()})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'album_confirm_delete.html', {'album': album})
