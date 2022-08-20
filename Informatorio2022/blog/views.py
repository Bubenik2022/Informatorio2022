from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context = {"insert_me": "I am from views.py",
                'prueba_variable': 'Probandooooooo'}
    return render(request,'index.html',context=context)

def contacto(request):
    ig = '@instagram'
    fc = 'facebook'
    tw = 'twitter'
    tel = 'telefono'
    email = 'email@email.com'
    return render(request,'contacto.html',context={'ig':ig,
                                                    'fc':fc,
                                                    'tw':tw,
                                                    'tel':tel,
                                                    'email':email,
                                                    })

def about(request):
    return render(request,'about.html')
