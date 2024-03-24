from django.shortcuts import render
from app_MJ.models import Produto

def base(request):
    produtos = Produto.objects.all()
    return render(request, 'base.html', {'produtos': produtos})

def sobre(request):
    return render(request, "sobre.html", {'sobre': 'active'})

def contato(request):
    return render(request, "contato.html", {'contato': 'active'})