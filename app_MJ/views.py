from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from app_MJ.models import *

@cache_page(30)

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

def sobre(request):
    return render(request, "sobre.html", {'sobre': 'active'})

def contato(request):
    return render(request, "contato.html", {'contato': 'active'})

def produto_detalhe(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)    
    return render(request, 'produto_detalhe.html', {'produto': produto})



