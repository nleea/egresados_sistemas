from rest_framework import serializers
from ....models import Inscripcion, Asistencia, Eventos
from ..BaseSerializers import BaseSerializers
from ...serializers.eventos.eventos_serialziers import EventosSerializersView
from .....auth_module.api.serializers.user.users_serializers import UserSerializersSimple


class InscripcionesSerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    evento = EventosSerializersView(read_only=True)
    user = UserSerializersSimple(read_only=True, many=True)

    def __init__(self, instance=None, data=..., **kwargs):
        expands = bool(kwargs.pop("expands", False))
        super().__init__(instance, data, **kwargs)

        if not expands:
            self.fields.pop("user")
            self.fields.pop("id")


class InscripcionesSerializers(BaseSerializers):
    evento = serializers.IntegerField()
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        inscripcion = Inscripcion.objects.create(
            evento_id=validated_data["evento"])
        inscripcion.user.set(validated_data["user"])
        return inscripcion

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.visible = validated_data.get('visible', instance.visible)
        instance.save()
        return instance


class AsistenciaSerializerView(BaseSerializers):
    evento = EventosSerializersView(read_only=True)
    user = serializers.IntegerField(read_only=True)

    class Meta:
        fields = "__all__"


class AsistenciaSerializer(BaseSerializers):
    evento = serializers.IntegerField()
    user = serializers.IntegerField()
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):

        evento_create_user = Eventos.objects.get(
            id=validated_data["evento"]).userCreate

        if evento_create_user and evento_create_user.pk != validated_data["user_session"].pk:
            raise Exception("Invalid")

        asistencia = Asistencia.objects.create(
            evento_id=validated_data["evento"], user_id=validated_data["user"], userCreate_id=validated_data["user_session"].pk)
        return asistencia

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.visible = validated_data.get('visible', instance.visible)
        instance.save()
        return instance
