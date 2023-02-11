from rest_framework import serializers
from ....models.models import Asignacion,User,Pqrs
from ..BaseSerializers import BaseSerializers

class AsignacionSerializers(BaseSerializers):
    funcionarioId = serializers.SlugRelatedField("username",read_only=True)
    pqrs = serializers.SlugRelatedField("description",read_only=True)


    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        funcionarioId = User.objects.get(pk=validated_data["funcionarioId"])
        pqrs = Pqrs.objects.get(pk=validated_data["pqrs"])
        userCreate = None
        if "userCreate" in validated_data:
            userCreate = validated_data["userCreate"]
        return Asignacion.objects.create(funcionarioId=funcionarioId,pqrs=pqrs,userCreate=userCreate)

    def update(self, instance, validated_data):
        try:
            newfuncionarioId = User.objects.get(pk=validated_data["funcionarioId"])
            instance.funcionarioId = newfuncionarioId
            instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
            instance.save()
            return instance
        except User.DoesNotExist as e:
            raise serializers.ValidationError(e.args[0])
        
