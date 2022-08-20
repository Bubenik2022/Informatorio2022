from django.urls import path

from . import views

urlpatterns = [
    path('',views.index , name="home"),
    path('noticias/', views.index, name='noticias'),
    path('contacto/',views.contacto , name='contacto'),
    path('nosotros/',views.about , name='nosotros'),
    path('<int:postid>/',views.single_post, name='post'),
    path('test/',views.post_list,name='test'),
]