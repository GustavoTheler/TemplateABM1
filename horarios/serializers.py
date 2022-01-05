from rest_framework import serializers
from horarios.models import Docente

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ['id', 'nombre', 'apellido']

    