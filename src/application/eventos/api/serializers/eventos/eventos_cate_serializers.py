from rest_framework import serializers
from ....models import EventosArea
from src.application.default.base_serializer import BaseSerializers

class EventosCategorySerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()

class EventosCategorySerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    visible = serializers.BooleanField(required=False,write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        evento = EventosArea.objects.create(
            name=validated_data["name"], userCreate=validated_data["userCreate"])
        return evento

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.visible = validated_data.get('visible', instance.visible)
        instance.save()
        return instance
