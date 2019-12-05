from django.db import models

class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True )
    nome = models.CharField(max_length=100, null = False)
    sigla = models.CharField(max_length=10, null = False)

    def __str__(self):
        return '{}, {}, {}'.format(self.codigo,self.nome, self.sigla)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.nome, self.sigla)

    pass


class Produto(models.Model):

    codigo = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100, null=False)
    preco = models.FloatField(null = False)
    quantidade = models.IntegerField(null = False)


    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,
                                  null= True)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.codigo, self.nome, self.preco,
                                       self.quantidade)

    def __repr__(self):
        return '{}, {}, {}, {}'.format(self.codigo, self.nome, self.preco,
                                       self.quantidade)

    pass
