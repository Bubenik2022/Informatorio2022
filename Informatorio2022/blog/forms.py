from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Comentario, Post
from django.contrib.auth.models import User


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)


class PostearForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'texto', 'imagen')