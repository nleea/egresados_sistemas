from rest_framework import serializers
from ....models import Inscripcion, Asistencia, Eventos
from ...serializers.eventos.eventos_serialziers import EventosSerializersView
from .....auth_module.api.serializers.user.users_serializers import (
    UserSerializersSimple,
)
from src.application.default.base_serializer import BaseSerializers

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
    evento = serializers.IntegerField(write_only=True)
    user = serializers.IntegerField(write_only=True)
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        inscripcion = Inscripcion.objects.create(
            evento_id=validated_data["evento"], user_id=validated_data["user"]
        )
        return inscripcion

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.visible = validated_data.get("visible", instance.visible)
        instance.save()
        return instance


class AsistenciaSerializerView(BaseSerializers):
    evento = EventosSerializersView(read_only=True)
    user = serializers.IntegerField(read_only=True)

    class Meta:
        fields = "__all__"


class ConfirmAsistenciaSerializer(BaseSerializers):
    evento = serializers.IntegerField()
    user = serializers.IntegerField()
    visible = serializers.BooleanField(required=False, write_only=True)
    asistencia = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            asistencia = Asistencia.objects.create(
                evento_id=validated_data["evento"],
                user_id=validated_data["user"],
                confirm=True,
            )
            return asistencia
        except Exception as e:
            raise serializers.ValidationError(e.args)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.visible = validated_data.get("visible", instance.visible)
        instance.save()
        return instance


class AsistenciaSerializer(BaseSerializers):
    evento = serializers.IntegerField()
    user = serializers.IntegerField()
    visible = serializers.BooleanField(required=False, write_only=True)
    asistencia = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        evento_create_user = Eventos.objects.get(id=validated_data["evento"]).userCreate

        if (
            evento_create_user
            and evento_create_user.pk != validated_data["user_session"].pk
        ):
            raise Exception("Invalid")

        try:
            asistencia = Asistencia.objects.create(
                evento_id=validated_data["evento"],
                user_id=validated_data["user"],
                userCreate_id=validated_data["user_session"].pk,
            )
            return asistencia
        except Exception as e:
            raise serializers.ValidationError(e.args)

    def update(self, instance, validated_data):
        evento_create_user = Eventos.objects.get(id=validated_data["evento"]).userCreate

        if (
            evento_create_user
            and evento_create_user.pk != validated_data["user_session"].pk
        ):
            raise Exception("Invalid")

        instance.name = validated_data.get("name", instance.name)
        instance.visible = validated_data.get("visible", instance.visible)
        instance.asistencia = validated_data.get("asistencia", instance.asistencia)
        instance.save()
        return instance
