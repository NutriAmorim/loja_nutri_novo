from django.shortcuts import render

def pagina_principal(request):
    return render(request, 'loja_app/pagina_principal.html')

def receitas_medicinais(request):
    return render(request, 'loja_app/receitas_medicinais.html')

def pesquisas(request):
    return render(request, 'loja_app/pesquisas_cientificas.html')

def quem_sou_eu(request):
    return render(request, 'loja_app/quem_sou_eu.html')

def quem_somos_nos(request):
    return render(request, 'loja_app/quem_somos_nos.html')
