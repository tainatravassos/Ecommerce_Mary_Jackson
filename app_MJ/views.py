from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from app_MJ.forms import ClienteForm
from django.db.models import Q
from app_MJ.models import *


@cache_page(30)

def home(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'produtos': produtos, 'categorias': categorias})

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
    categoria_slug = request.GET.get('categoria', None)
    categoria = None

    if categoria_slug:
        print(categoria_slug)
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        produtos = Produto.objects.filter(categoria=categoria).order_by('nome_produto')
    else:     
        produtos = Produto.objects.all().order_by('nome_produto')
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

def categorias(request):
    categorias = Categoria.objects.all().order_by('nome')
    return render(request, 'categorias.html', {'categorias': categorias})

def carrinho(request):
    # Lógica para recuperar os itens do carrinho e renderizar o template do carrinho
    return render(request, 'carrinho.html')

def pagamento(request):
    # Lógica para processar o pagamento e renderizar o template de pagamento
    return render(request, 'pagamento.html')

