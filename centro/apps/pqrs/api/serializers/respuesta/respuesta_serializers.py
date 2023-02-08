from rest_framework import serializers
from ....models.models import Pqrs,Respuesta,Anexo
from ..BaseSerializers import BaseSerializers

class RespuestaSerializers(BaseSerializers):
    pqrs = serializers.SlugRelatedField("description",read_only=True)
    anexo = serializers.SlugRelatedField("nombre_ane",read_only=True)

    def __init__(self, instance=None, data=..., **kwargs):
        meta = bool(kwargs.pop('meta', None))
        
        super().__init__(instance, data, **kwargs)
        
        if meta != True or meta is None:
            self.fields.pop("createdAt")
            self.fields.pop("updateAt")
            self.fields.pop("userCreate")
            self.fields.pop("userUpdate")

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            anexo = Anexo.objects.get(pk=validated_data["anexo"])
            pqrs = Pqrs.objects.get(pk=validated_data["pqrs"])
            userCreate = None
            if "userCreate" in validated_data:
                userCreate = validated_data["userCreate"]
            return Respuesta.objects.create(anexo=anexo,pqrs=pqrs,userCreate=userCreate)
        except (Anexo.DoesNotExist,Pqrs.DoesNotExist) as e:
            raise serializers.ValidationError(e.args[0])

    def update(self, instance, validated_data):
        try:
            anexo = Anexo.objects.get(pk=validated_data["anexo"])
            instance.anexo = anexo
            instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
            instance.save()
            return instance
        except Anexo.DoesNotExist as e:
            raise serializers.ValidationError(e.args[0])
