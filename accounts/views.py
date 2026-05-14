from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegistoForm
from .models import PerfilMagico
import secrets
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponse

# ---- LOGIN NORMAL (POR SENHA) ----
def login_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio_index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portfolio_index')
    else:
        form = AuthenticationForm()
    return render(request, 'portfolio/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('portfolio_index')

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('portfolio_index')
    else:
        form = RegistoForm()
    return render(request, 'portfolio/login.html', {'form': form, 'titulo': 'Registo'})

def login_magic_link(request):
    mensagem = None
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            perfil, created = PerfilMagico.objects.get_or_create(user=user)
            perfil.token = secrets.token_urlsafe(32)
            perfil.save()
            
            # ESTA LINHA ABAIXO É A QUE CORRIGE O LINK NO CODESPACES:
            # No accounts/views.py, dentro de login_magic_link:
            # No accounts/views.py, dentro de login_magic_link, apaga a linha do link antigo e usa esta:

            link = f"https://fantastic-space-fishstick-69p9g97qxq97crwpj-8000.app.github.dev/contas/autentica/?token={perfil.token}"
            
            # ATENÇÃO AO ALINHAMENTO DO SEND_MAIL:
            send_mail(
                subject='Autenticação Mágica',
                message=f'Caro {user.first_name}, clique no link para entrar: {link}',
                from_email='rodrigonascimento5b@gmail.com', # Usa o teu email real aqui
                recipient_list=[email],
            )
            mensagem = "Email enviado! Verifique a sua caixa de entrada."
        else:
            mensagem = "Email não encontrado."
    return render(request, 'portfolio/login_magic.html', {'mensagem': mensagem})
def autentica_view(request):
    token_url = request.GET.get('token')
    if token_url:
        try:
            perfil = PerfilMagico.objects.get(token=token_url)
            login(request, perfil.user)
            perfil.token = None # Limpa o token por segurança
            perfil.save()
            return redirect('portfolio_index')
        except PerfilMagico.DoesNotExist:
            return HttpResponse("Link inválido ou expirado.")
    return HttpResponse("Token não fornecido.")