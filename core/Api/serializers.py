from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristco


class PontoTuristcoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristco
        fields = ('id', 'nome', 'descricao')
