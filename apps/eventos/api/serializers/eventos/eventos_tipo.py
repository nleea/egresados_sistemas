from rest_framework import serializers
from ....models import TipoEvento
from ..BaseSerializers import BaseSerializers

class TipoEventosSerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)

class TipoEventosSerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        tipo_evento = TipoEvento.objects.create(
            name=validated_data["name"], userCreate=validated_data["userCreate"])
        return tipo_evento

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.save()
        return instance
