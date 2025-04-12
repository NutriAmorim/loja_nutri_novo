from django.db import models

class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos/')
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)