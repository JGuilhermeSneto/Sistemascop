
from django.urls import path, include
from .views import index,perfil

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    
]
