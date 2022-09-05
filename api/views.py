from rest_framework import permissions
from rest_framework import viewsets

from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ComunicacaoPerdaViewSet(viewsets.ModelViewSet):
    queryset = ComunicacaoPerda.objects.all()
    serializer_class = ComunicacaoPerdaSerializer
    # permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def grafico(request):
    print()
    graficos = [
        {"nome": "CHUVA EXCESSIVA", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="CHUVA EXCESSIVA"))},
        {"nome": "GEADA", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="GEADA"))},
        {"nome": "GRANIZO", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="GRANIZO"))},
        {"nome": "SECA", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="SECA"))},
        {"nome": "VENDAVAL", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="VENDAVAL"))},
        {"nome": "RAIO", "quantidade": len(ComunicacaoPerda.objects.filter(evento_ocorrido="RAIO"))},
    ]
    return Response(graficos)
