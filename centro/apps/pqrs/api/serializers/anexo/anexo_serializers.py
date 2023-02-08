from rest_framework import serializers
from ....models.models import Anexo
from ..BaseSerializers import BaseSerializers

class AnexoSerializers(BaseSerializers):
    nombre_ane = serializers.CharField()

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
        userCreate = None
        if "userCreate" in validated_data:
            userCreate = validated_data["userCreate"]
        return Anexo.objects.create(nombre_ane=validated_data["nombre_ane"],userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.nombre_ane = validated_data.get('nombre_ane', instance.nombre_ane)
        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance
