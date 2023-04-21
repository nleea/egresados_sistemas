from rest_framework import serializers
from ....models.models import Pqrs,Respuesta
from ..BaseSerializers import BaseSerializers

class RespuestaSerializers(BaseSerializers):
    pqrs = serializers.SlugRelatedField("description",read_only=True)
    descripcion = serializers.CharField()
    anexo = serializers.FileField()
    
    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            userCreate = None
            if "userCreate" in validated_data:
                userCreate = validated_data["userCreate"]
            return Respuesta.objects.create(descripcion=validated_data["descripcion"],pqrs_id=validated_data["pqrs"],userCreate=userCreate,anexo=validated_data["anexo"])
        except Pqrs.DoesNotExist as e:
            raise serializers.ValidationError(e.args[0])

    def update(self, instance, validated_data):
        try:
            instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(e.args[0])


class RespuestaPqrsSerializers(BaseSerializers):
    descripcion = serializers.CharField()
    
    class Meta:
        fields = "__all__"