from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
import os

def pagina_principal(request):
    return render(request, 'loja_app/pagina_principal.html')

@login_required
def receitas_medicinais(request):
    return render(request, 'loja_app/receitas_medicinais.html')

@login_required
def pesquisas(request):
    return render(request, 'loja_app/pesquisas_cientificas.html')

@login_required
def quem_sou_eu(request):
    return render(request, 'loja_app/quem_sou_eu.html')

@login_required
def quem_somos_nos(request):
    return render(request, 'loja_app/quem_somos_nos.html')

@login_required
def suplementos(request):
    return render(request, 'loja_app/suplementos.html')

@login_required
def vitaminas(request):
    return render(request, 'loja_app/vitaminas.html')

@login_required
def cuidado_pessoal(request):
    return render(request, 'loja_app/cuidado_pessoal.html')

@login_required
def beleza(request):
    return render(request, 'loja_app/beleza.html')

@login_required
def casa_saudavel(request):
    return render(request, 'loja_app/casa_saudavel.html')

@login_required
def pets(request):
    return render(request, 'loja_app/pets.html')

@login_required
def alimentos(request):
    return render(request, 'loja_app/alimentos.html')

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Faz login automático após cadastro
            messages.success(request, 'Cadastro realizado com sucesso!')
            # Redirecionar para a página que o usuário estava antes, ou página principal
            return redirect(request.GET.get('next', 'pagina_principal'))
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = UserCreationForm()
    return render(request, 'loja_app/cadastro.html', {'form': form})

def robots_txt(request):
    if settings.DEBUG:
        return HttpResponse("User-agent: *\nDisallow: /", content_type='text/plain')
    else:
        robots_path = os.path.join(settings.BASE_DIR, 'loja_app', 'robots.txt')
        with open(robots_path, 'r') as file:
            return HttpResponse(file.read(), content_type='text/plain')
