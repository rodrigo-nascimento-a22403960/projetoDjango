from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistoForm

def login_view(request):
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
            login(request, user) # Faz login automático após registo
            return redirect('portfolio_index')
    else:
        form = RegistoForm()
    return render(request, 'portfolio/login.html', {'form': form, 'titulo': 'Registo'})