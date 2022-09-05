from rest_framework import serializers

from .models import *


class ComunicacaoPerdaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComunicacaoPerda
        fields = ['id', 'data_cadastro', 'nome', 'email', 'cpf', 'longitude', 'latitude', 'tipo_lavoura', 'data_colheira', 'evento_ocorrido']

