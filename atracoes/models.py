from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    decricao = models.TextField()
    horario = models.TextField()
    idade_minima = models.IntegerField()

    def __str__(self):
        return self.nome
