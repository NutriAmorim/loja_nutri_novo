from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from loja_app.sitemaps import StaticViewSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'static': StaticViewSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="loja_app/robots.txt", content_type="text/plain")),

    # Login e logout
    path('login/', auth_views.LoginView.as_view(template_name='loja_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

# Adicionando a configuração para servir arquivos estáticos e de mídia
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
