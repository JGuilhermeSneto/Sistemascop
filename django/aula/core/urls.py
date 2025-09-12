
from django.urls import path, include
from .views import index,perfil,contato

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('contato/', contato, name='contato'),
    
]
