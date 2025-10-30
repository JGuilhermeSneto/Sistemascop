from django.urls import path
from .views import index, contato, perfil

urlpatterns = [
    path('', index, name = 'index'),
    path('contato/', contato, name = 'contato'),
    path('perfil/', perfil, name = 'perfil' )
]