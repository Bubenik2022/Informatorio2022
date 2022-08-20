from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.

def index(request):
    context = {"insert_me": "I am from views.py",
                'prueba_variable': 'Probandooooooo'}
    return render(request,'index.html',context=context)

def contacto(request):
    ig = '@instagram'
    fc = 'orquestavientosdecambio'
    tw = 'twitter'
    ubi = 'Roque Sáenz Peña, Chaco, Argentina'
    telhiper = '549'+'03644574664'
    tel = '03644-574664'
    email = 'orquestaescuelavientosdecambio@gmail.com'
    return render(request,'contacto.html',context={'ig':ig,
                                                    'fc':fc,
                                                    'tw':tw,
                                                    'ubi':ubi,
                                                    'telhiper':telhiper,
                                                    'tel':tel,
                                                    'email':email,
                                                    })

def about(request):
    return render(request,'about.html')

def post_list(request):
    ls = Post.objects.all()
    context = {'post_list': ls,
                'id':Post.objects.get(id=1)
                }
    return render(request,'single-post.html',context)

def single_post(request,postid):
    return render(request,'single-post.html',{'post':Post.objects.get(id=postid)})
