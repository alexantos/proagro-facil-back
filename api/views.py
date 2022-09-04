from rest_framework import permissions
from rest_framework import viewsets

from .serializers import *


class ComunicacaoPerdaViewSet(viewsets.ModelViewSet):
    queryset = ComunicacaoPerda.objects.all()
    serializer_class = ComunicacaoPerdaSerializer
    # permission_classes = [permissions.IsAuthenticated]
