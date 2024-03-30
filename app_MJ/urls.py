from django.urls import path
from app_MJ.views import home, sobre, contato, cadastro_produto

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato"),
    path('cadastro-produto/', cadastro_produto, name="cadastro_produto")
]
