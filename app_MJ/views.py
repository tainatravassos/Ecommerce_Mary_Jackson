from django.shortcuts import render
from app_MJ.forms import ProdutoForm
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

def cadastro_produto(request):
    produto = Produto.objects.all()
    form = ProdutoForm(request.POST or None)
    success = False
    error = False
    if form.is_valid():
        form.save()
        success = True
    else:
        error = True
    context = {
        'form': form,
        'success': success,
        'error': error,
        'produto': produto,
    }
    return render(request, "cadastro_produto.html", context)    