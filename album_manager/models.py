from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    año_lanzamiento = models.PositiveIntegerField()
    genero = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)


    def __str__(self):
        return self.titulo
