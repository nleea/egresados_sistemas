from rest_framework import serializers
from ....models.models import Categoria
from src.application.default.base_serializer import BaseSerializers

class CategorySerializersView(BaseSerializers):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

class CategorySerializers(BaseSerializers):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    visible = serializers.BooleanField(required=False,write_only=True)


    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Categoria.objects.create(name=validated_data["name"],userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.visible = validated_data.get('visible', instance.visible)

        instance.save()
        return instance
