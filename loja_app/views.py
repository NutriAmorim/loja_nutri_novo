from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages  # Adicione esta linha
import os

def pagina_principal(request):
    if request.user.is_authenticated:
        messages.info(request, f"Bem-vindo(a), {request.user.username}!")  # Agora messages está definido
    return render(request, 'loja_app/pagina_principal.html')

# Páginas públicas
def receitas_medicinais(request):
    return render(request, 'loja_app/receitas_medicinais.html')

def pesquisas(request):
    return render(request, 'loja_app/pesquisas_cientificas.html')

def quem_sou_eu(request):
    return render(request, 'loja_app/quem_sou_eu.html')

def quem_somos_nos(request):
    return render(request, 'loja_app/quem_somos_nos.html')

def suplementos(request):
    return render(request, 'loja_app/suplementos.html')

def vitaminas(request):
    return render(request, 'loja_app/vitaminas.html')

def cuidado_pessoal(request):
    return render(request, 'loja_app/cuidado_pessoal.html')

def beleza(request):
    return render(request, 'loja_app/beleza.html')

def casa_saudavel(request):
    return render(request, 'loja_app/casa_saudavel.html')

def pets(request):
    return render(request, 'loja_app/pets.html')

def alimentos(request):
    return render(request, 'loja_app/alimentos.html')

# Cadastro de usuário
def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Faz login automático após cadastro
            return redirect('pagina_principal')  # Redireciona direto para a home
    
        else:
         messages.error(request, "Erro ao cadastrar. Verifique os dados informados.")
    else:
        form = UserCreationForm()
    return render(request, 'loja_app/cadastro.html', {'form': form})

# Servindo o arquivo robots.txt
def robots_txt(request):
    robots_path = os.path.join(settings.BASE_DIR, 'loja_app', 'robots.txt')
    with open(robots_path, 'r') as file:
        return HttpResponse(file.read(), content_type='text/plain')
