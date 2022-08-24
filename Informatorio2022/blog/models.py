from time import time
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    nombre_evento = models.CharField(max_length=200)
    fecha_hora_evento = models.DateField(auto_now=False, auto_now_add=False)
    informacion = models.CharField(max_length=200)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def eliminar(self):
        self.fecha_eliminacion = timezone.now()
        self.delete()                                      #lo elimina de la base de datos también? sip

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)   #importa el orden en el que se crean los modelos? está bien definida esta FK?
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='')
    texto = models.TextField()  
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-fecha_publicacion',)

    def __str__(self):
        return 'Comentado por {}'.format(self.autor)

'''class Imagen(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length = 200)

class Video(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)'''


    
    
