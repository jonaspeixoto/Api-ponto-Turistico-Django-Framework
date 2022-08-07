from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristco
from .serializers import PontoTuristcoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristco.objects.all()
    serializer_class = PontoTuristcoSerializer
