from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_app.urls')),  # Inclui as URLs do app loja_app
]