from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.IntegerField(default=0)
    qntd = models.IntegerField()

    def __str__(self):
        return self.nome

