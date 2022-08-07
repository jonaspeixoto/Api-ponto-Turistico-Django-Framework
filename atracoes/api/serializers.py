from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracoesSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id','nome', 'decricao', 'horario', 'idade_minima')
