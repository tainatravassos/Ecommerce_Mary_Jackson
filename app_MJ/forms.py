from django import forms
from app_MJ.models import *

class ClienteForm(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ['nome_completo', 'endereco', 'cidade', 'estado', 'telefone', 'email', 'senha']
    widgets = {'senha': forms.PasswordInput()}
    
  
