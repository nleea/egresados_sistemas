from rest_framework import serializers
from ....models.models import Seccion

class SeccionSerializers(serializers.Serializer):
    name = serializers.CharField()
    
    
    class Meta:
        fields = "__all__"
    
    def create(self, validated_data):
        return Seccion(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance