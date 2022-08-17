from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context = {"insert_me": "I am from views.py",
                'prueba_variable': 'Probandooooooo'}
    return render(request,'index.html',context=context)