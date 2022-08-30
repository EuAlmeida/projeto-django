from re import M
from tkinter.tix import INTEGER
from django.db import models


class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email_usuario = models.EmailField(null=False)
    nome_usuario = models.TextField(null=False, max_length=60)
    telefone_usuario = models.PositiveIntegerField(null=False)
    data_nascimento = models.DateField(null=False)
    senha_user = models.CharField(null=False, max_length=12)
    endereco_user = models.CharField(null=False, max_length=30)

    def __str__(self):
        return self.nome_usuario
