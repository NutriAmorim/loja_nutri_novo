from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from loja_app.sitemaps import StaticViewSitemap
from django.contrib.auth import views as auth_views  # <-- Importa as views de login/logout

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='loja_app/login.html'), name='login'),  # <-- Rota de login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # <-- Rota de logout
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
