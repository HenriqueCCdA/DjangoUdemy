from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=180)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
