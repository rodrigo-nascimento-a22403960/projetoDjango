from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='portfolio_index'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('makingof/', views.makingof_view, name='makingof'),
]