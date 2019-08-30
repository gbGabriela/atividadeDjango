from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome    = models.CharField(max_length=50, verbose_name="Digite seu nome completo")
    cpf     = models.CharField(verbose_name="cpf", max_length=11, verbose_name="Insira seu CPF")
    email   = models.EmailField(max_length=100, max_length=11, verbose_name="Insira seu email")

    def __str__(self):
        return self.nome + " - " + self.cpf + " - " + self.email

class Professor(models.Model):
    nome        = models.CharField(max_length=50, verbose_name="Digite seu nome completo")
    areaAtuacao = models.CharField(max_length=100, max_length=11, verbose_name="Descreva sua área de atuaçao")
    cpf         = models.CharField(verbose_name="cpf", max_length=11, max_length=11, verbose_name="Insira seu CPF")
    email       = models.EmailField(max_length=100, max_length=11, verbose_name="Insira seu email")

    def __str__(self):
        return self.nome + " - " + self.areaAtuacao + " -" + self.cpf + " - " + self.email

class Curso(models.Model):
    tema        = models.CharField(max_length=50, verbose_name="Insira o tema do curso")
    assunto     = models.CharField(verbose_name="cpf", max_length=11, verbose_name="Insira o assunto do curso")
    descricao   = models.TextField(verbose_name="Descrição do curso")
    duracao     = models.DataField(verbose_name="Duração do curso")

    def __str__(self):
        return self.tema + " - " + self.assunto + " - " + self.descricao+ " - " + str(self.duracao)

class Inscricao(models.Model):
    dataInscricao = models.DateField(verbose_name="Data d insrição")

    def __str__(self):
        return str(self.dataInscricao)

class Certificado(models.Model):
    dataConclusao = models.DateField(verbose_name="Data da conclusão")

    def __str__(self):
        return str(self.dataConclusao)
