from django import forms
from .models import Categoria

class CategoriaForm(forms.Form):
    codigo = forms.IntegerField(required= False)
    nome = forms.CharField(max_length=100,
                           label='Digite o nome ')
    sigla = forms.CharField(max_length=100,
                            label='Digite a sigla ')
    pass

class ProdutoForm(forms.Form):
    codigo = forms.IntegerField(required=False)
    nome = forms.CharField(max_length=100,
                           label='Digite o nome ')
    preco = forms.FloatField(label='Digite o preço ')
    quantidade = forms.IntegerField(label='Digite a quantidade ')

    categoria = forms.ModelChoiceField(queryset= Categoria.objects.all(),
                                       empty_label='Selecione a Categoria')


    pass


