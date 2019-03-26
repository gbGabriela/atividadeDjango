from django.urls import path
from metodoAvaliacao.views import IndexView

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
]
