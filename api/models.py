from django.db import models


class ComunicacaoPerda(models.Model):
    data_cadastro = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    cpf = models.CharField(max_length=16)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)  # localizacao_lavoura
    latitude = models.DecimalField(max_digits=8, decimal_places=3)
    tipo_lavoura = models.CharField(max_length=16)
    data_colheira = models.DateTimeField()
    evento_ocorrido = models.CharField(max_length=16)
