from rest_framework import viewsets

from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import calculaDistancia


class ComunicacaoPerdaViewSet(viewsets.ModelViewSet):
    queryset = ComunicacaoPerda.objects.all()
    serializer_class = ComunicacaoPerdaSerializer


@api_view(['GET'])
def grafico(request):
    graficos = [
        {"nome": "CHUVA EXCESSIVA", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="CHUVA EXCESSIVA"))},
        {"nome": "GEADA", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="GEADA"))},
        {"nome": "GRANIZO", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="GRANIZO"))},
        {"nome": "SECA", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="SECA"))},
        {"nome": "VENDAVAL", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="VENDAVAL"))},
        {"nome": "RAIO", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="RAIO"))},
    ]
    return Response(graficos)


@api_view(['GET'])
def verifica_distancia(request, id):
    perda_parametro = ComunicacaoPerda.objects.get(id=id)
    # FIXME Melhorar verificação de data
    perdas = ComunicacaoPerda.objects.filter(data_cadastro__day=perda_parametro.data_cadastro.day, data_cadastro__month=perda_parametro.data_cadastro.month, data_cadastro__year=perda_parametro.data_cadastro.year)
    for perda_banco in perdas:
        if not perda_banco.evento_ocorrido == perda_parametro.evento_ocorrido:
            distancia = calculaDistancia(
                latitude1=perda_parametro.latitude,
                longitude1=perda_parametro.longitude,
                latitude2=perda_banco.latitude,
                longitude2=perda_banco.longitude,
                unit='kilometers'
            )
            if distancia <= 10:
                return Response({'distancia_menor': True})
            else:
                return Response({'distancia_menor': False})
    return Response({})
