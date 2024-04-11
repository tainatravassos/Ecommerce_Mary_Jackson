from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.contrib.auth import logout
from app_MJ.forms import ClienteForm
from django.db.models import Q
from django.shortcuts import redirect
from app_MJ.models import *


@cache_page(30)

def home(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    carrinho = Carrinho.objects.all()
    return render(request, 'home.html', {'produtos': produtos, 'categorias': categorias, 'carrinho': carrinho})

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

def categorias(request):
    categorias = Categoria.objects.all().order_by('nome')
    return render(request, 'categorias.html', {'categorias': categorias})

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

def logout_usuario(request):
    logout(request)
    return redirect('home')

def login_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Cliente.objects.filter(email=email, senha=senha).exists():
            return render(request, 'home.html',{'usuario': Cliente.objects.all()})
        else:
            return HttpResponse('Usuário não cadastrado')
    else:
        return HttpResponse('Método não permitido')


def carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carro_id = request.session.get('carro_id')
    if carro_id:
        carro_obj = Carrinho.objects.get(id=carro_id)
    else:
        carro_obj = Carrinho.objects.create(total=0)
        request.session['carro_id'] = carro_obj.id
    return render(request, 'carrinho.html', {'produto': produto, 'carrinho': carro_obj})


def carrinhoproduto(request):
    carrinhoprodutos = CarrinhoProduto.objects.all()
    return render(request, 'carrinhoproduto.html', {'carrinhoprodutos': carrinhoprodutos})

def deletar_item_carrinho(request, carrinhoproduto_id):
    carrinhoproduto = get_object_or_404(CarrinhoProduto, pk=carrinhoproduto_id)
    carrinhoproduto.delete()
    return redirect('carrinhoproduto')
