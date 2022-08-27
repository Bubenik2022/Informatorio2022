import os
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from blog.models import Post, Comentario
from blog.forms import ComentarioForm
from django.views.generic import DetailView
from django.contrib import messages
from blog.forms import ComentarioForm, PostearForm
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    ls = list(Post.objects.all().order_by('-id'))
    context = {'post_list': ls,
                }
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
    ls = list(Post.objects.all().order_by('-id'))
    context = {'post_list': ls,
                }
    return render(request,'test.html',context)


class DetallesPost(DetailView):

    model = Post
    template_name = 'single-post.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comentarios_conectados = Comentario.objects.filter(
            post=self.get_object()).order_by('-fecha_publicacion')

        data['comentarios'] = comentarios_conectados

        if self.request.user.is_authenticated:
            data['comentario_form'] = ComentarioForm(instance=self.request.user)

        return data
    
    def post(self, request, *args, **kwargs):
        nuevo_comentario = Comentario(texto=request.POST.get('texto'),
                                  autor=self.request.user,
                                  post=self.get_object())
        nuevo_comentario.save()
        return self.get(self, request, *args, **kwargs)

'''def single_post(request,postid,slug):

    comentario_form = ComentarioForm()
    
    context = {
        'post': Post.objects.get(id=postid),
        'comentario_form': comentario_form,

                }
    return render(request,'single-post.html',context)'''

'''def crear_post(request):
    if request.method == "POST":
        form = FormPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user.id
            post.save()
            titulo = form.cleaned_data.get("title")
            messages.success(request, f"El post {titulo} se ha creado correctamente")
            return redirect("post")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    form = FormPost()
    return render(request, "crear_post.html", {"form": form})'''

class Postear(CreateView):
    model = Post
    template_name = 'crear_post.html'
    fields = ('titulo','texto')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            data['post_form'] = PostearForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
            nuevo_post = Post(texto=request.POST.get('texto'),
                                    autor=self.request.user,
                                    titulo=self.request.POST.get('titulo')
                                    )
            nuevo_post.save()

            return self.get(self, request, *args, **kwargs)


class EditarPost(UpdateView):
    model = Post
    template_name = 'editar_post.html'
    fields = ('titulo','texto','imagen')

class EliminarPost(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('home')
    