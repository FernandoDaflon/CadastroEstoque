from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .forms import *

def home(request):
    template = loader.get_template('appEstoque/home.html')
    return HttpResponse(template.render())
    pass

def criar_categoria(request):
    forms = CategoriaForm()
    return render(request, 'appEstoque/cadastrarcategoria.html',
                  {'forms':  forms})
    pass

def cadastrar_categoria(request):
    try:
        if request.method == 'POST':
            form = CategoriaForm(request.POST or None)
            if form.is_valid():
                categoria = Categoria()
                categoria.nome = form.cleaned_data['nome']
                categoria.sigla = form.cleaned_data['sigla']
                categoria.save()
                msg = 'Categoria cadastrada com sucesso'
                return render(request, 'appEstoque/cadastrarcategoria.html',
                              {'forms': CategoriaForm(), 'msg': msg})

            else:
                msg = form.errors
                return render(request, 'appEstoque/cadastrarcategoria.html',
                              {'forms': form, 'msg': msg})
        else:
            raise Exception('Use Post para formularios',
                            'MethodEnvioError')

    except Exception as ex:
        msg = ex
        return render(request, 'appEstoque/cadastrarcategoria.html',
                      {'forms': CategoriaForm(), 'msg': msg})