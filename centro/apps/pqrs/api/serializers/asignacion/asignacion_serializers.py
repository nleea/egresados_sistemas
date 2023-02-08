from rest_framework import serializers
from ....models.models import Asignacion,User,Pqrs
from ..BaseSerializers import BaseSerializers

class AsignacionSerializers(BaseSerializers):
    funcionarioId = serializers.SlugRelatedField("username",read_only=True)
    pqrs = serializers.SlugRelatedField("description",read_only=True)

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
        
