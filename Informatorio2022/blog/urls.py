from django.urls import path

from . import views

urlpatterns = [
    path('',views.index , name="home"),
    path('noticias/', views.index, name='noticias'),
    path('contacto/',views.contacto , name='contacto'),
    path('nosotros/',views.about , name='nosotros'),
    path('<int:postid>/<slug:slug>/',views.DetallesPost.as_view(), name='post'),
    #path('crear_post/',  views.crear_post, name='crear_post'),
    path('crear_post/',views.Postear.as_view(), name='crear_post'),
    
    path('test/',views.post_list,name='test'), #dejar último
]