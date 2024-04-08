from django.contrib import admin
from.models import *


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)  
    ordering = ('nome',)  
    
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto',  'categoria')
    ordering = ('nome_produto', 'categoria')

admin.site.register(Cliente)
admin.site.register(Carrinho)
admin.site.register(CarrinhoProduto)
admin.site.register(Pedido_order)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
