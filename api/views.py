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
    #Testar corretamente esse método
    for perda_banco in ComunicacaoPerda.objects.filter(data_cadastro=perda_parametro.data_cadastro).exclude(evento_ocorrido=perda_parametro.evento_ocorrido):
        distancia = getDistanceBetweenPointsNew(
            latitude1=perda_parametro.latitude,
            longitude1=perda_parametro.longitude,
            latitude2=perda_banco.latitude,
            longitude2=perda_banco.longitude,
            unit='kilometers'
        )
        print(distancia)
        if distancia <= 10:
            print("Comunica analista")
        else:
            print("Segue o baile")
    return Response({})


from numpy import sin, cos, arccos, pi, round


def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees


def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians


def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2, unit='miles'):
    theta = longitude1 - longitude2

    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) +
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )

    if unit == 'miles':
        return round(distance, 2)
    if unit == 'kilometers':
        return round(distance * 1.609344, 2)
