from rest_framework import serializers
from ....models import SubAreaEventos
from ..BaseSerializers import BaseSerializers


class EventosSubAreaSerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    area = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)

    def __init__(self, instance=None, data=..., **kwargs):
        expanded = bool(kwargs.pop("expands", True))
        
        super().__init__(instance, data, **kwargs)

        if not expanded:
            self.fields.pop("area")
        

    class Meta:
        fields = "__all__"


class EventosSubAreaSerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    area = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        evento = SubAreaEventos.objects.create(
            name=validated_data["name"], area_id=validated_data["area"], userCreate=validated_data["userCreate"])
        return evento

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.area_id = validated_data.get(
            'area', instance.area)
        instance.save()
        return instance
