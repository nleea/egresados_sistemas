from rest_framework import serializers
from ....models.models import TipoMomento
from ..BaseSerializers import BaseSerializers

class MomentSerializers(BaseSerializers):
    tipo = serializers.CharField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return TipoMomento.objects.create(tipo=validated_data["tipo"],userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance
