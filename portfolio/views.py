from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import models as auth_models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Licenciatura, UnidadeCurricular, Tecnologia, Competencia, Formacao, Projeto, TFC, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import models as auth_models
from django.contrib.auth.decorators import login_required

# ---- AUTENTICAÇÃO ----

def registo_view(request):
    if request.method == "POST":
        auth_models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'portfolio/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('projetos')
        else:
            return render(request, 'portfolio/login.html', {'mensagem': 'Credenciais inválidas'})
    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    return redirect('projetos')


# ---- CRUD PROJETOS (protegido) ----

@login_required
def projeto_criar(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Novo Projeto'})

@login_required
def projeto_editar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Projeto'})

@login_required
def projeto_apagar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': projeto, 'titulo': 'Apagar Projeto'})


# ---- CRUD TECNOLOGIAS (protegido) ----

@login_required
def tecnologia_criar(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Tecnologia'})

@login_required
def tecnologia_editar(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Tecnologia'})

@login_required
def tecnologia_apagar(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': tecnologia, 'titulo': 'Apagar Tecnologia'})


# ---- CRUD COMPETÊNCIAS ----

@login_required
def competencia_criar(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Competência'})

@login_required
def competencia_editar(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Competência'})

@login_required
def competencia_apagar(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': competencia, 'titulo': 'Apagar Competência'})


# ---- CRUD FORMAÇÕES (protegido) ----

@login_required
def formacao_criar(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Formação'})

@login_required
def formacao_editar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Formação'})

@login_required
def formacao_apagar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': formacao, 'titulo': 'Apagar Formação'})