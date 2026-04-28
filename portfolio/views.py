from django.shortcuts import render
from .models import Licenciatura, UnidadeCurricular, Tecnologia, Competencia, Formacao, Projeto, TFC, MakingOf

def index_view(request):
    return render(request, 'portfolio/index.html')

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('unidadecurricular_set').all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias', 'competencias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def makingof_view(request):
    makingof = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingof': makingof})