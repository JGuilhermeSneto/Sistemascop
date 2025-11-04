from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=100)
    nome_completo = models.CharField('Nome completo', max_length=100)

    USERNAME_FIELD = 'username'