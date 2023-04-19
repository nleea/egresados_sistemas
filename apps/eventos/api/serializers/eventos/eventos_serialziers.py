from rest_framework import serializers
from ....models import Eventos
from ..BaseSerializers import BaseSerializers


class EventosSerializersView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    area = serializers.SlugRelatedField("name", read_only=True)
    subArea = serializers.SlugRelatedField("name", read_only=True)
    nombre_actividad = serializers.CharField()
    tipo_actividad = serializers.CharField()
    responsable = serializers.SlugRelatedField("username", read_only=True)
    fecha = serializers.DateTimeField(read_only=True)
    hora = serializers.CharField()
    lugar = serializers.CharField()
    cupos = serializers.IntegerField()
    descripcion = serializers.CharField()
    objectivo = serializers.CharField()

    class Meta:
        fields = "__all__"


class EventosSerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    area = serializers.IntegerField()
    subArea = serializers.IntegerField()
    nombre_actividad = serializers.CharField()
    tipo_actividad = serializers.CharField()
    responsable = serializers.IntegerField()
    fecha = serializers.DateTimeField(read_only=True)
    hora = serializers.CharField()
    lugar = serializers.CharField()
    cupos = serializers.IntegerField()
    descripcion = serializers.CharField()
    objectivo = serializers.CharField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):

        try:
            evento = Eventos.objects.create(area_id=validated_data["area"],
                                        descripcion=validated_data["descripcion"], subArea_id=validated_data["subArea"],
                                        tipo_actividad=validated_data["tipo_actividad"],
                                        nombre_actividad=validated_data[
                                            "nombre_actividad"], responsable_id=validated_data["responsable"], lugar=validated_data[
                                            "lugar"], hora=validated_data["hora"], userCreate=validated_data["userCreate"],
                                        cupos=validated_data["cupos"], objectivo=validated_data["objectivo"])
            return evento
        except BaseException as e:
            raise

        

    def update(self, instance, validated_data):
        instance.area_id = validated_data.get(
            'area', instance.area)
        instance.descripcion = validated_data.get(
            'descripcion', instance.descripcion)
        instance.subArea_id = validated_data.get(
            'subArea', instance.subArea)
        instance.nombre_actividad = validated_data.get(
            'nombre_actividad', instance.nombre_actividad)
        instance.responsable_id = validated_data.get(
            'responsable_id', instance.responsable_id)
        instance.fecha = validated_data.get(
            'fecha', instance.fecha)
        instance.lugar = validated_data.get(
            'lugar', instance.lugar)
        instance.userCreate_id = validated_data.get(
            'userCreate', instance.userCreate)
        instance.cupos = validated_data.get(
            'cupos', instance.cupos)
        instance.objectivo = validated_data.get(
            'objectivo', instance.objectivo)
        instance.save()
        return instance
