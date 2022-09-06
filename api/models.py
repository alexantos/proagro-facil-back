from django.db import models


class ComunicacaoPerda(models.Model):
    data_cadastro = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    cpf = models.CharField(max_length=16)
    longitude = models.FloatField()  # localizacao_lavoura
    latitude = models.FloatField()
    tipo_lavoura = models.CharField(max_length=16)
    data_colheira = models.DateTimeField()
    evento_ocorrido = models.CharField(max_length=16)
