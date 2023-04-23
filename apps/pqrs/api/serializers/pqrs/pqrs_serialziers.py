from rest_framework import serializers
from ....models.models import Pqrs
from ..BaseSerializers import BaseSerializers

class PqrsSerializersView(BaseSerializers):
    titulo = serializers.CharField()
    description = serializers.CharField()
    persona = serializers.SlugRelatedField("username", read_only=True)
    tipopqrs = serializers.SlugRelatedField("tipo", read_only=True)
    status = serializers.CharField(
        source="get_status_display", read_only=True)
    anexo = serializers.FileField(required=False)


class PqrsSerializers(BaseSerializers):
    titulo = serializers.CharField()
    description = serializers.CharField()
    persona = serializers.SlugRelatedField("username", read_only=True)
    tipopqrs = serializers.SlugRelatedField("name", read_only=True)
    tipopqrs = serializers.IntegerField(write_only=True)
    persona = serializers.IntegerField(write_only=True)
    status = serializers.CharField(write_only=True,required=False)
    status_display = serializers.CharField(
        source="get_status_display", read_only=True)
    anexo = serializers.FileField(required=False)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            anexo = None
            if 'anexo' in validated_data:
                anexo = validated_data["anexo"]
            return Pqrs.objects.create(description=validated_data["description"], titulo=validated_data["titulo"], tipopqrs_id=validated_data["tipopqrs"], persona_id=validated_data["persona"], userCreate=validated_data["userCreate"],anexo=anexo)
        except Exception as e:
            a = serializers.ValidationError(e.args)
            raise a

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.userUpdate = validated_data.get(
            "userUpdate", instance.userUpdate)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance


class PqrsRespuestaSerializers(BaseSerializers):
    titulo = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        fields = "__all__"
