from django.urls import path
from metodoAvaliacao.views import *

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('curriculo/', CurriculoView.as_view(), name="curriculo"),
	path('sobre/', SobreView.as_view(), name="sobre"),
	path('cadastro/', CadastroView.as_view(), name="cadastro"),

	#Professor
	path('cadastro/professor', CadastrarProfessor.as_view(), name="cadastro-professor"),
	path('listar/professor', ListarProfessor.as_view(), name="listar-professor"),
	path('excluir/professor/<int:pk>/', ExcluirProfessor.as_view(), name="excluir-professor"),
	path('editar/professor/<int:pk>/', AtualizarProfessor.as_view(), name="editar-professor"),

	# Aluno
	path('cadastro/aluno', CadastrarAluno.as_view(), name="cadastro-aluno"),
	path('listar/aluno', ListarAluno.as_view(), name="listar-aluno"),
	path('excluir/aluno/<int:pk>', ExcluirAluno.as_view(), name="excluir-aluno"),
	path('alterar/aluno/<int:pk>', AtualizarAluno.as_view(), name="editar-aluno"),

	# Curso
	path('cadastro/curso', CadastrarCurso.as_view(), name="cadastro-curso"),
	path('listar/curso', ListarCurso.as_view(), name="listar-curso"),
	path('excluir/curso/<int:pk>', ExcluirCurso.as_view(), name="excluir-curso"),
	path('alterar/curso/<int:pk>', AtualizarCurso.as_view(), name="editar-curso"),

	# Inscrição
	path('cadastro/inscricao', CadastrarInscricao.as_view(), name="cadastro-inscricao"),
	path('listar/inscricao', ListarInscricao.as_view(), name="listar-inscricao"),
	path('excluir/inscricao/<int:pk>', ExcluirIncricao.as_view(), name="excluir-inscricao"),
	path('alterar/inscricao/<int:pk>', AtualizarInscricao.as_view(), name="editar-inscricao"),

	# Certificado
	path('cadastro/certificado', CadastrarCertificado.as_view(), name="cadastro-certificado"),
	path('listar/certificado', ListarCertificado.as_view(), name="listar-certificado"),
	path('excluir/certificado/<int:pk>', ExcluirCertificado.as_view(), name="excluir-certificado"),
	path('alterar/certificado/<int:pk>', AtualizarCertificado.as_view(), name="editar-certificado"),

]
