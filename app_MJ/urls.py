from django.urls import path
from app_MJ.views import home, sobre, contato, produto_detalhe, busca, produtos

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato"),
    path('produto-detalhe/<int:produto_id>', produto_detalhe, name="produto_detalhe"),
    path('busca/', busca, name='busca'),
    path('produtos/', produtos, name='produtos'),
]
