from time import time
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publcacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publcacion = timezone.now()
        self.save()
    
    def __str__(self):
        return self.titulo

class Imagen(models.Model):
    descripcion = models.CharField(max_length = 200)

class Video(models.Model):
    descripcion = models.CharField(max_length=200)

class evento(models.Model):
    titulo = models.CharField(max_length=200)
    nombre_evento = models.CharField(max_length=200)
    fecha_hora_evento = models.DateField(auto_now=False, auto_now_add=False)
    fecha_hora_pub_evento = models.DateField(auto_now=False, auto_now_add=True)
    fecha_hora_elim_evento = models.DateField(auto_now=False, auto_now_add=True)
    informacion = models.CharField(max_length=200)
        