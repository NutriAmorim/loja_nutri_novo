from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from loja_app.sitemaps import StaticViewSitemap

# Instanciando o sitemap
sitemaps = {
    'static': StaticViewSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
