from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('receitas/', views.receitas_medicinais, name='receitas_medicinais'),
    path('pesquisas/', views.pesquisas, name='pesquisas_cientificas'),
    path('quem-sou-eu/', views.quem_sou_eu, name='quem_sou_eu'),
    path('quem-somos-nos/', views.quem_somos_nos, name='quem_somos_nos'),
    path('suplementos/', views.suplementos, name='suplementos'),    
    path('vitaminas/', views.vitaminas, name='vitaminas'),
    path('cuidado-pessoal/', views.cuidado_pessoal, name='cuidado_pessoal'),
    path('beleza/',views.beleza, name='beleza'),
    path('casa-saudavel/', views.casa_saudavel, name='casa_saudavel'),
    path('pets/',views.pets, name='pets'),
    path('alimentos/', views.alimentos, name='alimentos'),
    path('login/', auth_views.LoginView.as_view(template_name='loja_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('robots.txt', views.robots_txt, name='robots_txt'),  # ✅ Adicionado
]
