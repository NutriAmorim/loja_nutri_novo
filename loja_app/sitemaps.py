from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'pagina_principal',
            'receitas_medicinais',
            'pesquisas_cientificas',
            'quem_sou_eu',
            'quem_somos_nos',
        ]

    def location(self, item):
        return reverse(item)
