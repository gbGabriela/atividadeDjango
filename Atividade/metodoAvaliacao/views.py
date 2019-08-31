from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Professor, Aluno, Curso, Inscricao, Certificado

class IndexView(TemplateView):
    template_name = "index.html"

class CurriculoView(TemplateView):
    template_name = "curriculo.html"

class SobreView(TemplateView):
    template_name = "sobre.html"

class CadastrarProfessor(LoginRequiredMixin, CreateView):
    model           = Professor
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-professor')
    login_url       = reverse_lazy('login')
    fields          = ['nome', 'areaAtuacao', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context                 = super(CadastrarProfessor, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Cadastrar como professor"
        context['botao']        = "Cadastrar"
        context ['classeBotao'] = "btn-primary"
        return context

class ExcluirProfessor(LoginRequiredMixin, DeleteView):
    model          = Professor
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-professor')
    login_url       = reverse_lazy('login')
    fields          = ['nome', 'areaAtuacao', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context                 = super(ExcluirProfessor, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Excluir cadastro de professor"
        context['botao']        = "Excluir"
        context ['classeBotao'] = "btn-danger"
        return context

class AtualizarProfessor(LoginRequiredMixin, UpdateView):
    model          = Professor
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-professor')
    login_url       = reverse_lazy('login')
    fields          = ['nome', 'areaAtuacao', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context                 = super(AtualizarProfessor, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Atualizar o cadastro  de professor"
        context['botao']        = "Atualizar"
        context ['classeBotao'] = "btn-success"
        return context

class ListarProfessor(LoginRequiredMixin, ListView):
    model          = Professor
    template_name   = "lista/lista-professor.html"

class CadastrarAluno(LoginRequiredMixin, CreateView):
    model           = Aluno
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-aluno')
    login_url       = reverse_lazy('login')
    fields          = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context                 = super(CadastrarAluno, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Cadastrar como aluno"
        context['botao']        = "Cadastrar"
        context ['classeBotao'] = "btn-primary"
        return context

class ExcluirAluno(LoginRequiredMixin, DeleteView):
    model          = Aluno
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-aluno')
    login_url       = reverse_lazy('login')
    fields          = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context                 = super(ExcluirAluno, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Excluir cadastro de aluno"
        context['botao']        = "Excluir"
        context ['classeBotao'] = "btn-danger"
        return context

class AtualizarAluno(LoginRequiredMixin, UpdateView):
    model          = Aluno
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-aluno')
    login_url       = reverse_lazy('login')
    fields          = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context                 = super(AtualizarAluno, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Atualizar o cadastro  de aluno"
        context['botao']        = "Atualizar"
        context ['classeBotao'] = "btn-success"
        return context

class ListarAluno(LoginRequiredMixin, ListView):
    model          = Aluno
    template_name   = "lista/lista-aluno.html"

class CadastrarCurso(LoginRequiredMixin, CreateView):
    model           = Curso
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-curso')
    login_url       = reverse_lazy('login')
    fields          = ['tema', 'assunto', 'descricao', 'duracao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(CadastrarCurso, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Cadastrar o curso"
        context['botao']        = "Cadastrar"
        context ['classeBotao'] = "btn-primary"
        return context

class ExcluirCurso(LoginRequiredMixin, DeleteView):
    model          = Curso
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-curso')
    login_url       = reverse_lazy('login')
    fields          = ['tema', 'assunto', 'descricao', 'duracao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(ExcluirCurso, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Excluir cadastro de curso"
        context['botao']        = "Excluir"
        context ['classeBotao'] = "btn-danger"
        return context

class AtualizarCurso(LoginRequiredMixin, UpdateView):
    model          = Curso
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-curso')
    login_url       = reverse_lazy('login')
    fields          = ['tema', 'assunto', 'descricao', 'duracao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(AtualizarCurso, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Atualizar o cadastro de curso"
        context['botao']        = "Atualizar"
        context ['classeBotao'] = "btn-success"
        return context

class ListarCurso(LoginRequiredMixin, ListView):
    model          = Curso
    template_name   = "lista/lista-curso.html"

class CadastrarInscricao(LoginRequiredMixin, CreateView):
    model           = Inscricao
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-inscricao')
    login_url       = reverse_lazy('login')
    fields          = ['dataInscricao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(CadastrarInscricao, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Fazer a inscrição"
        context['botao']        = "Cadastrar"
        context ['classeBotao'] = "btn-primary"
        return context

class ExcluirIncricao(LoginRequiredMixin, DeleteView):
    model           = Inscricao
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-inscricao')
    login_url       = reverse_lazy('login')
    fields          = ['dataInscricao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(ExcluirIncricao, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Excluir a inscrição"
        context['botao']        = "Excluir"
        context ['classeBotao'] = "btn-danger"
        return context

class AtualizarInscricao(LoginRequiredMixin, UpdateView):
    model           = Inscricao
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-inscricao')
    login_url       = reverse_lazy('login')
    fields          = ['dataInscricao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(AtualizarInscricao, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Atualizar o cadastro de inscrição"
        context['botao']        = "Atualizar"
        context ['classeBotao'] = "btn-success"
        return context

class ListarInscricao(LoginRequiredMixin, ListView):
    model          = Inscricao
    template_name   = "lista/lista-inscricao.html"

class CadastrarCertificado(LoginRequiredMixin, CreateView):
    model           = Certificado
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-certificado')
    login_url       = reverse_lazy('login')
    fields          = ['dataConclusao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(CadastrarCertificado, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Cadastrar certificado"
        context['botao']        = "Cadastrar"
        context ['classeBotao'] = "btn-primary"
        return context

class ExcluirCertificado(LoginRequiredMixin, DeleteView):
    model           = Certificado
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-certificado')
    login_url       = reverse_lazy('login')
    fields          = ['dataConclusao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(ExcluirCertificado, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Excluir certificado"
        context['botao']        = "Excluir"
        context ['classeBotao'] = "btn-danger"
        return context

class AtualizarCertificado(LoginRequiredMixin, UpdateView):
    model           = Certificado
    template_name   = "formulario.html"
    success_url     = reverse_lazy('listar-certificado')
    login_url       = reverse_lazy('login')
    fields          = ['dataConclusao']
    def get_context_data(self, *args, **kwargs):
        context                 = super(AtualizarCertificado, self).get_context_data(*args, **kwargs)
        context['titulo']       = "Atualizar certificado"
        context['botao']        = "Atualizar"
        context ['classeBotao'] = "btn-success"
        return context

class ListarCertificado(LoginRequiredMixin, ListView):
    model          = Certificado
    template_name   = "lista/lista-certificado.html"
