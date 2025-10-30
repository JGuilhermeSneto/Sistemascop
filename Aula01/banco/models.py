from django.db import models

# Create your models here.

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)
    def __str__(self):
        return self.nome
     


class Instrutor(models.Model):
    nome = models.CharField('Nome', max_length=300)
    def __str__(self):
        return self.nome

class Publico(models.Model):
    nome = models.CharField('Nome', max_length= 300)
    def __str__(self):
        return self.nome


class Cursos(models.Model):
    titulo = models.CharField('Curso',max_length=100)
    descricao = models.TextField('Descrição')
    vagas = models.IntegerField('Número de vagas', null=True)
    instrutor = models.ForeignKey(Instrutor,on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)
         