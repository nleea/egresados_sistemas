from rest_framework import serializers
from ....models.models import Pqrs,User,TipoPqrs
from ..BaseSerializers import BaseSerializers
from ..pqrs.tipo_serializers import PqrsTipoSerializers

class PqrsSerializers(BaseSerializers):
    description = serializers.CharField()
    persona = serializers.SlugRelatedField("username",read_only=True)
    tipopqrs = serializers.SlugRelatedField("tipo",read_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        persona = User.objects.get(pk=validated_data["persona"])
        tipo = TipoPqrs.objects.get(pk=validated_data["tipo"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Pqrs.objects.create(description=validated_data["description"],tipopqrs=tipo,persona=persona,userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance
