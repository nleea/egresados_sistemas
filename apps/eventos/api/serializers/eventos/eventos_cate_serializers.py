from rest_framework import serializers
from ....models import EventosArea
from ..BaseSerializers import BaseSerializers

class EventosCategorySerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()

class EventosCategorySerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        evento = EventosArea.objects.create(
            name=validated_data["name"], userCreate=validated_data["userCreate"])
        return evento

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.save()
        return instance
