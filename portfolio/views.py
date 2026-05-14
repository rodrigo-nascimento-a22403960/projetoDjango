from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Licenciatura, UnidadeCurricular, Tecnologia, Competencia, Formacao, Projeto, TFC, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm


# ---- SEGURANÇA (VERIFICAÇÃO DE GRUPO) ----
def is_gestor(user):
    return user.groups.filter(name='gestor-portfolio').exists()


# ---- VIEWS DE LISTAGEM ----

def index_view(request):
    return redirect('projetos')

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

def sobre_view(request):
    tecnologias = Tecnologia.objects.all()
    makingofs = MakingOf.objects.all()
    
    return render(request, 'portfolio/sobre.html', {
        'tecnologias': tecnologias,
        'makingofs': makingofs
    })


# ---- CRUD PROJETOS ----

@login_required
@user_passes_test(is_gestor)
def projeto_criar(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/forms.html', {'form': form, 'titulo': 'Novo Projeto'})

@login_required
@user_passes_test(is_gestor)
def projeto_editar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/forms.html', {'form': form, 'titulo': 'Editar Projeto'})

@login_required
@user_passes_test(is_gestor)
def projeto_apagar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': projeto, 'titulo': 'Apagar Projeto'})


# ---- CRUD TECNOLOGIAS ----

@login_required
@user_passes_test(is_gestor)
def tecnologia_criar(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/forms.html', {'form': form, 'titulo': 'Nova Tecnologia'})

@login_required
@user_passes_test(is_gestor)
def tecnologia_editar(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/forms.html', {'form': form, 'titulo': 'Editar Tecnologia'})

@login_required
@user_passes_test(is_gestor)
def tecnologia_apagar(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': tecnologia, 'titulo': 'Apagar Tecnologia'})


# ---- CRUD COMPETÊNCIAS ----

@login_required
@user_passes_test(is_gestor)
def competencia_criar(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/forms.html', {'form': form, 'titulo': 'Nova Competência'})

@login_required
@user_passes_test(is_gestor)
def competencia_editar(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/forms.html', {'form': form, 'titulo': 'Editar Competência'})

@login_required
@user_passes_test(is_gestor)
def competencia_apagar(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': competencia, 'titulo': 'Apagar Competência'})


# ---- CRUD FORMAÇÕES ----

@login_required
@user_passes_test(is_gestor)
def formacao_criar(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/forms.html', {'form': form, 'titulo': 'Nova Formação'})

@login_required
@user_passes_test(is_gestor)
def formacao_editar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/forms.html', {'form': form, 'titulo': 'Editar Formação'})

@login_required
@user_passes_test(is_gestor)
def formacao_apagar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': formacao, 'titulo': 'Apagar Formação'})