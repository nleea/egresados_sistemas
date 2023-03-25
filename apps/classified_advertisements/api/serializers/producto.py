from rest_framework import serializers
from ...models.models import Producto
from .BaseSerializers import BaseSerializers


class ProductoSerializers(BaseSerializers):
    cantidad = serializers.CharField()
    name = serializers.CharField()
    precio = serializers.CharField()
    
        
    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        return Producto.objects.create(cantidad=validated_data["cantidad"],precio=validated_data["precio"],name=validated_data["name"])

    def update(self, instance, validated_data):
        instance.cantidad = validated_data.get('cantidad', instance.cantidad)
        instance.name = validated_data.get('name', instance.name)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.save()
        return instance