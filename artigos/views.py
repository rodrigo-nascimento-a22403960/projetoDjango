from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

# ---- REGISTO ----
def registo_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo, created = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo)
            login(request, user)
            return redirect('artigos_lista') 
    else:
        form = UserCreationForm()
    return render(request, 'artigos/registo.html', {'form': form})

# ---- SEGURANÇA ----
def is_autor(user):
    return user.groups.filter(name='autores').exists()

# ---- LISTAGEM E DETALHE ----
def artigos_lista(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/lista.html', {'artigos': artigos})

def artigo_detalhe(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    
    # Gerir a submissão de um novo comentário
    form = ComentarioForm()
    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('artigo_detalhe', id=id)
            
    return render(request, 'artigos/detalhe.html', {'artigo': artigo, 'comentarios': comentarios, 'form': form})

def artigo_like(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    artigo.likes += 1
    artigo.save()
    return redirect('artigo_detalhe', id=artigo.id)

# ---- CRUD ARTIGOS (Protegido) ----
@login_required
@user_passes_test(is_autor)
def artigo_criar(request):
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user # Associa o artigo a quem está logado!
        artigo.save()
        return redirect('artigos_lista')
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Novo Artigo'})

@login_required
@user_passes_test(is_autor)
def artigo_editar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    
    # REGRA DE OURO: Só o próprio autor pode editar!
    if artigo.autor != request.user:
        return HttpResponseForbidden("Acesso Negado: Apenas o autor deste artigo o pode editar.")
        
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigo_detalhe', id=artigo.id)
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Editar Artigo'})