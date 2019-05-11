from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class CurriculoView(TemplateView):
    template_name = "curriculo.html"

class SobreView(TemplateView):
    template_name = "sobre.html"

class CadastroView(TemplateView):
    template_name = "cadastro.html"
