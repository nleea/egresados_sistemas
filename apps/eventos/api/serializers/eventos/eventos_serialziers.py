from rest_framework import serializers
from ....models import Eventos
from ..BaseSerializers import BaseSerializers
from .eventos_sub_area_serializers import EventosSubAreaSerializersView
from .eventos_cate_serializers import EventosCategorySerializersView
from .eventos_tipo import TipoEventosSerializersView


class EventosAsistenciaSerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    area = EventosCategorySerializersView(read_only=True)
    subArea = EventosSubAreaSerializersView(read_only=True, expands=False)
    nombre_actividad = serializers.CharField(read_only=True)
    tipo = TipoEventosSerializersView(read_only=True)
    responsable = serializers.CharField(read_only=True)
    fecha = serializers.DateField(read_only=True)
    hora = serializers.CharField(read_only=True)
    lugar = serializers.CharField(read_only=True)
    cupos = serializers.IntegerField(read_only=True)
    descripcion = serializers.CharField(read_only=True)
    objectivo = serializers.CharField(read_only=True)
    confirm_asistencia = serializers.BooleanField(read_only=True)
    fecha_pasada = serializers.BooleanField(read_only=True)
    asistire = serializers.BooleanField(read_only=True)

    def to_representation(self, instance):
        resulst = super().to_representation(instance)
        resulst["tipo_actividad"] = {"id": instance.tipo.id, "name": instance.tipo.name}
        resulst["subArea"] = {**resulst["subArea"], "area": {**resulst["area"]}}
        del resulst["tipo"]
        return resulst

    class Meta:
        fields = "__all__"


class EventosSerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    area = EventosCategorySerializersView(read_only=True)
    subArea = EventosSubAreaSerializersView(read_only=True, expands=False)
    nombre_actividad = serializers.CharField(read_only=True)
    tipo = TipoEventosSerializersView(read_only=True, meta=False)
    responsable = serializers.CharField(read_only=True)
    fecha = serializers.DateField(read_only=True)
    hora = serializers.CharField(read_only=True)
    lugar = serializers.CharField(read_only=True)
    cupos = serializers.IntegerField(read_only=True)
    descripcion = serializers.CharField(read_only=True)
    objectivo = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        resulst = super().to_representation(instance)
        resulst["tipo_actividad"] = {"id": instance.tipo.id, "name": instance.tipo.name}
        resulst["subArea"] = {**resulst["subArea"], "area": {**resulst["area"]}}
        del resulst["tipo"]
        return resulst

    class Meta:
        fields = "__all__"


class EventosSerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    area = serializers.IntegerField()
    subArea = serializers.IntegerField()
    nombre_actividad = serializers.CharField()
    tipo_actividad = serializers.IntegerField()
    responsable = serializers.CharField()
    fecha = serializers.DateField()
    hora = serializers.CharField()
    lugar = serializers.CharField()
    cupos = serializers.IntegerField()
    descripcion = serializers.CharField()
    objectivo = serializers.CharField()
    userCreate = serializers.SlugRelatedField("username", read_only=True)
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            evento = Eventos.objects.create(
                area_id=validated_data["area"],
                descripcion=validated_data["descripcion"],
                subArea_id=validated_data["subArea"],
                tipo_id=validated_data["tipo_actividad"],
                fecha=validated_data["fecha"],
                nombre_actividad=validated_data["nombre_actividad"],
                responsable=validated_data["responsable"],
                lugar=validated_data["lugar"],
                hora=validated_data["hora"],
                userCreate=validated_data["userCreate"],
                cupos=validated_data["cupos"],
                objectivo=validated_data["objectivo"],
            )

            return evento
        except BaseException as e:
            raise e

    def update(self, instance, validated_data):
        instance.area_id = validated_data.get("area", instance.area)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.subArea_id = validated_data.get("subArea", instance.subArea)
        instance.tipo_id = validated_data.get("tipo_actividad", instance.tipo)
        instance.nombre_actividad = validated_data.get(
            "nombre_actividad", instance.nombre_actividad
        )
        instance.responsable = validated_data.get("responsable", instance.responsable)
        instance.fecha = validated_data.get("fecha", instance.fecha)
        instance.hora = validated_data.get("hora", instance.hora)
        instance.lugar = validated_data.get("lugar", instance.lugar)
        instance.cupos = validated_data.get("cupos", instance.cupos)
        instance.objectivo = validated_data.get("objectivo", instance.objectivo)
        instance.userCreate = validated_data.get("userCreate", instance.userCreate)
        instance.visible = validated_data.get("visible", instance.visible)
        instance.save()
        return instance
