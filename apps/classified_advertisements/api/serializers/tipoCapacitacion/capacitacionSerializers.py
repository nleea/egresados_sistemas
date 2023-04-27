from rest_framework import serializers
from ....models.models import TiposCapacitaciones
from ..BaseSerializers import BaseSerializers

class CapacitacionesSerializersView(BaseSerializers):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

class CapacitacionesSerializers(BaseSerializers):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
        
    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return TiposCapacitaciones.objects.create(name=validated_data["name"],userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.userUpdate = validated_data.get('userUpdate', instance.userUpdate)
        instance.save()
        return instance