from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('receitas/', views.receitas_medicinais, name='receitas_medicinais'),
    path('pesquisas/', views.pesquisas, name='pesquisas_cientificas'),
    path('quem-sou-eu/', views.quem_sou_eu, name='quem_sou_eu'),
    path('quem-somos-nos/', views.quem_somos_nos, name='quem_somos_nos'),
    path('robots.txt', views.robots_txt, name='robots_txt'),  # ✅ Adicionado
]
