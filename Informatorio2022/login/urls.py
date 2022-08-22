from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('registro/',UserRegisterView.as_view(),name='registro'),
    
]