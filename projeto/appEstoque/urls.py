from django.urls import path
from .import views

app_name = 'appEstoque'

urlpatterns = [
    # http://127.0.0.1:8000/Estoque/
    path('', views.home, name='home'),
    path('Categoria/', views.criar_categoria, name='categoria'),
    path('CadCategoria/', views.cadastrar_categoria, name='cadcategoria')
]