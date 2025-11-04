from django.urls import path
from .views import Autenticacao,Perfil,Desconectar

urlpatterns = [
    path('Autenticacao/', Autenticacao, name='Autenticacao'),
    path('Desconectar/', Desconectar, name='Desconectar'),
    path('Perfil/', Perfil, name='Perfil')
]
