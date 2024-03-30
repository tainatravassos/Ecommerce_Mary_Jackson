from django import forms
from app_MJ.models import Produto

class ProdutoForm(forms.ModelForm):
  class Meta:
    model = Produto
    fields = ['nome_produto', 'slug', 'categoria', 'descricao', 'quantidade', 'imagem', 'preco']
