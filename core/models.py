from re import M
from tabnanny import verbose
from tkinter.tix import INTEGER
from unicodedata import name
from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email_usuario = models.EmailField(null=False)
    nome_usuario = models.TextField(null=False, max_length=60)
    telefone_usuario = models.PositiveIntegerField(null=False)
    data_nascimento = models.DateField(null=False)
    senha_user = models.CharField(null=False, max_length=12)
    endereco_user = models.CharField(null=False, max_length=30)

    def __str__(self):
        return self.nome_usuario

    class Meta:
        verbose_name_plural = "Usuários"


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=20, null=False)
    desc_categoria = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.nome_categoria


class Editora(models.Model):
    id_editora = models.AutoField(primary_key=True)
    nome_editora = models.CharField(max_length=30, null=False)
    cnpj_editora = models.PositiveIntegerField(null=False)
    email_editora = models.EmailField(null=False)
    senha_editora = models.CharField(max_length=12, null=False)
    endereço_editora = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nome_editora


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nome_autor = models.TextField(max_length=60, null=False)

    class Meta:
        verbose_name_plural = "Autores"


class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo_livro = models.CharField(max_length=30)
    sinopse_livro = models.CharField(max_length=450)
    numero_paginas = models.PositiveIntegerField(null=False)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livro")
    categoria = models.ManyToManyField(Categoria, related_name="livros")
    
    def __str__(self):
        return self.titulo_livro
