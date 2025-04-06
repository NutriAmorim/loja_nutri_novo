# loja_app/middleware.py
from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Chama a resposta do próximo middleware
        response = self.get_response(request)

        # Verifica o host
        host = request.get_host()

        # Verifica se o host não tem 'www.' e se está acessando via HTTPS
        if host and not host.startswith('www.') and request.is_secure():
            # Redireciona para a versão com 'www.' na URL
            return HttpResponsePermanentRedirect('https://www.' + host + request.get_full_path())

        return response
