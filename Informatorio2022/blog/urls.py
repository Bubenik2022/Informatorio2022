from django.urls import path

from . import views

urlpatterns = [
    path('',views.index , name="home"),
    path('noticias/', views.index, name='noticias'),
    path('contacto/',views.contacto , name='contacto'),
    path('nosotros/',views.about , name='nosotros'),
    path('post/<int:postid>/<slug:slug>/',views.DetallesPost.as_view(), name='post'),
    path('eliminar_post/<int:postid>/<slug:slug>',views.EliminarPost.as_view(), name='eliminar_post'),
    path('editar_post/<int:postid>/<slug:slug>',views.EditarPost.as_view(), name='editar_post'),
    path('crear_post/',views.Postear.as_view(), name='crear_post'),
    
    path('test/',views.post_list,name='test'), #dejar último
]