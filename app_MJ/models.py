from django.db import models
from datetime import datetime
from django import forms
from django.contrib.auth.models import User

class Cliente(models.Model):
    estados = (
        ('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO'), ('DF', 'DF'),    
    )

    nome_completo = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=4, choices=estados)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    telefone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True, unique=True)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_completo


class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome_produto = models.CharField(max_length=200, default='')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1) 
    descricao = models.TextField()
    quantidade = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to="", null=True, blank=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    #visualizacao = models.IntegerField(default=0)
    data_produto = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.nome_produto
    
    def imagem_url(self):
        if self.imagem:
            return self.imagem.url
        else:
            return None


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    data_pedido = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return f"Carrinho ID: {self.id} - Cliente: {self.cliente.nome_completo}"
    

class CarrinhoProduto(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    avaliacao = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    data_pedido = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return f"Carrinho: {self.carrinho.id} - CarrinhoProduto: {self.id} - Produto: {self.produto.nome_produto}"

PEDIDO_STATUS = (
    ('Pedido Recebido', 'Pedido Recebido'),
    ('Pedido em Processamento', 'Pedido em Processamento'),
    ('Pedido Enviado', 'Pedido Enviado'),
    ('Pedido Entregue', 'Pedido Entregue'),
    ('Pedido Cancelado', 'Pedido Cancelado'),
)


class Pedido_order(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    ordenando_por = models.CharField(max_length=200)
    endereco_envio = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    subtotal = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    data_pedido = models.DateTimeField(default=datetime.now, blank=True)
    desconto = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    telefone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    pedido_status = models.CharField(max_length=200, choices=PEDIDO_STATUS, default='Pedido Recebido')
    observacoes = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return f"Pedido_order: {self.id} - Cliente: {self.cliente.nome_completo} - Status: {self.pedido_status}"
