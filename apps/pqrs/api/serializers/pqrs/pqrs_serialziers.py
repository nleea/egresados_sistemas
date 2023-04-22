from rest_framework import serializers
from ....models.models import Pqrs, User, TipoPqrs
from ..BaseSerializers import BaseSerializers


class PqrsSerializers(BaseSerializers):
    titulo = serializers.CharField()
    description = serializers.CharField()
    persona = serializers.SlugRelatedField("username", read_only=True)
    tipopqrs = serializers.SlugRelatedField("tipo", read_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            return Pqrs.objects.create(description=validated_data["description"], titulo=validated_data["titulo"], tipopqrs_id=validated_data["tipo"], persona_id=validated_data["persona"], userCreate=validated_data["userCreate"])
        except (User.DoesNotExist, TipoPqrs.DoesNotExist) as e:
            a = serializers.ValidationError(e.args)
            print(a.detail)
            raise a

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.userUpdate = validated_data.get(
            "userUpdate", instance.userUpdate)
        instance.save()
        return instance


class PqrsRespuestaSerializers(BaseSerializers):
    titulo = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        fields = "__all__"
