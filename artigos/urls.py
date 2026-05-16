from django.urls import path
from . import views

urlpatterns = [
    path('registo/', views.registo_view, name='registo'),
    path('', views.artigos_lista, name='artigos_lista'), # <-- Era esta que o Django não estava a achar!
    path('novo/', views.artigo_criar, name='artigo_criar'),
    path('<int:id>/', views.artigo_detalhe, name='artigo_detalhe'),
    path('<int:id>/editar/', views.artigo_editar, name='artigo_editar'),
    path('<int:id>/like/', views.artigo_like, name='artigo_like'),
]