from rest_framework import serializers
from ....models.models import SubCategoria,Categoria,TiposCapacitaciones
from ..BaseSerializers import BaseSerializers
from ...serializers.category.category_serializers import CategorySerializers


class CapacitacionesSerializers(BaseSerializers):
    tipo = serializers.CharField()
    name = serializers.CharField()
        
    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return TiposCapacitaciones.objects.create(tipo=validated_data["tipo"],userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.name = validated_data.get('name', instance.name)
        instance.userUpdate = validated_data.get('userUpdate', instance.userUpdate)
        instance.save()
        return instance