from django.urls import path
from .views import Cadastro, dados

urlpatterns = [
    path('Cadastro/', Cadastro,name = 'Cadastro'),
    path('dados/', dados, name='dados'),

]
