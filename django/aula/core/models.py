from django.db import models

# Create your models here.

class Perfil(models.Model):
    nome = models.CharField(max_length = 200)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.CharField(max_length = 11)

    def __str__ (self):
        return self.nome