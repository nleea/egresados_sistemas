from rest_framework import serializers
from ....models.models import TipoPqrs
from src.application.default.base_serializer import BaseSerializers

class PqrsTipoSerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    tipo = serializers.CharField(read_only=True)


class PqrsTipoSerializers(BaseSerializers):
    tipo = serializers.CharField()
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return TipoPqrs.objects.create(
            tipo=validated_data["tipo"], userCreate=userCreate
        )

    def update(self, instance, validated_data):
        instance.tipo = validated_data.get("tipo", instance.tipo)
        instance.userUpdate = validated_data.get("userUpdate", instance.userUpdate)
        instance.visible = validated_data.get("visible", instance.visible)
        instance.save()
        return instance
