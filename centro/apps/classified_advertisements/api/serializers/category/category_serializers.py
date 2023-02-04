from rest_framework import serializers
from ..seccion.seccion_serializers import SeccionSerializers
from ....models.models import Categoria

class CategorySerializers(serializers.Serializer):
    name = serializers.CharField()
    seccionId = SeccionSerializers()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        return Categoria(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance