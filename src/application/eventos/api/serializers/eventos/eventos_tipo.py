from rest_framework import serializers
from ....models import TipoEvento
from src.application.default.base_serializer import BaseSerializers


class TipoEventosSerializersView(BaseSerializers):
    name = serializers.CharField(read_only=True)


class TipoEventosSerializers(BaseSerializers):
    name = serializers.CharField()
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        tipo_evento = TipoEvento.objects.create(
            name=validated_data["name"], userCreate=validated_data["userCreate"]
        )
        return tipo_evento

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.visible = validated_data.get("visible", instance.visible)
        instance.save()
        return instance
