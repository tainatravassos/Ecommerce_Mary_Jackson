from django.urls import path
from app_MJ.views import home, sobre, contato, produto_detalhe

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato"),
    path('produto-detalhe/<int:produto_id>', produto_detalhe, name="produto_detalhe"),
]
