from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()
router.register(r'perdas', ComunicacaoPerdaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('grafico/', grafico),
    path('distancia/<int:id>/', verifica_distancia),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
