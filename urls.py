# loja_nutri_novo/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from loja_app.sitemaps import StaticViewSitemap  # Certifique-se de que o arquivo existe!

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_app.urls')),  # Inclui as URLs do app loja_app
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
