from rest_framework import serializers
from ....models import Inscripcion,Asistencia
from ..BaseSerializers import BaseSerializers
from ...serializers.eventos.eventos_serialziers import EventosSerializersView
from .....auth_module.api.serializers.user.users_serializers import UserSerializersSimple


class InscripcionesSerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    evento = EventosSerializersView(read_only=True)
    user = UserSerializersSimple(read_only=True,many=True)


class InscripcionesSerializers(BaseSerializers):
    evento = serializers.IntegerField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        inscripcion = Inscripcion.objects.create(evento_id=validated_data["evento"])
        inscripcion.user.set(validated_data["user"])
        return inscripcion

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.save()
        return instance


class AsistenciaSerializer(BaseSerializers):
    evento = serializers.IntegerField()
    user = serializers.IntegerField()
    
    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        asistencia = Asistencia.objects.create(evento_id=validated_data["evento"],user_id=validated_data["user"])
        return asistencia

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.save()
        return instance
    