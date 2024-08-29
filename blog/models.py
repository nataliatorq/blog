# blog/models.py
from django.db import models

class GostosPessoais(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='gostos_pessoais/', null=True, blank=True)  # Atualize o campo imagem

    def __str__(self):
        return self.nome

class Curiosidades(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='curiosidades/', null=True, blank=True)  # Atualize o campo imagem

    def __str__(self):
        return self.nome

class SobreMim(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='sobre_mim/', null=True, blank=True)  # Adicione este campo

    def __str__(self):
        return self.nome