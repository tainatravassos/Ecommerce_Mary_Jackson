from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from app_MJ.forms import ClienteForm
from django.db.models import Q
from app_MJ.models import *


@cache_page(30)

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos})
def cestas(request):
    return render(request, 'cestas.html')

def sobre(request):
    return render(request, "sobre.html", {'sobre': 'active'})

def contato(request):
    return render(request, "contato.html", {'contato': 'active'})

def produto_detalhe(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)    
    return render(request, 'produto_detalhe.html', {'produto': produto})


def busca(request):
    termo_busca = request.GET.get('q')
    resultados = None

    if termo_busca and termo_busca.isdigit():
        resultados = Produto.objects.filter(id=termo_busca)
    else:
        if termo_busca:
            resultados = Produto.objects.filter(
                Q(nome_produto__icontains=termo_busca) 
            )

    return render(request, 'busca.html', {'resultados': resultados, 'termo_busca': termo_busca})

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def cadastro(request):
    user = Cliente.objects.all()
    form = ClienteForm(request.POST or None)
    success = False
    error = False
    if form.is_valid():
        form.save()
        success = True
        form.clean()
    else:
        error = True
    context = {
        'form': form,
        'success': success,
        'error': error,
        'user': user,
    }
    return render(request, "user.html", context)