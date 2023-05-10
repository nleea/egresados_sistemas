from rest_framework import serializers
from ....models.models import Asignacion, User, Pqrs
from ..BaseSerializers import BaseSerializers
from ..pqrs.pqrs_serialziers import PqrsSerializersView
from .....auth_module.api.serializers.user.users_serializers import UserSerializersSimple


class AsignacionSerializerView(BaseSerializers):
    # funcionarioId = UserSerializersSimple(read_only=True)
    pqrs = PqrsSerializersView(read_only=True,meta=False)


class AsignacionSerializers(BaseSerializers):
    # funcionarioId = serializers.IntegerField()
    pqrs = serializers.IntegerField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            userCreate = None
            if "userCreate" in validated_data:
                userCreate = validated_data["userCreate"]
            return Asignacion.objects.create(funcionarioId_id=validated_data["funcionarioId"], pqrs_id=validated_data["pqrs"], userCreate=userCreate)
        except (User.DoesNotExist, Pqrs.DoesNotExist) as e:
            raise serializers.ValidationError(e.args[0])

    def update(self, instance, validated_data):
        try:
            instance.funcionarioId_id = validated_data.get(
                "funcionarioId", instance.funcionarioId)
            instance.userUpdate = validated_data.get(
                "userUpdate", instance.userUpdate)
            instance.save()
            return instance
        except User.DoesNotExist as e:
            raise serializers.ValidationError(e.args[0])
