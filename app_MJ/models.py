from django.db import models
from datetime import datetime


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    foto = models.ImageField(upload_to="produtos", null=True, blank=True)
    data_produto = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome