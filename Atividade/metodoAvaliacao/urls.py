from django.urls import path
from metodoAvaliacao.views import *

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('curriculo/', CurriculoView.as_view(), name="curriculo"),
	path('sobre/', SobreView.as_view(), name="sobre"),
	path('cadastro/', CadastroView.as_view(), name="cadastro"),
]
