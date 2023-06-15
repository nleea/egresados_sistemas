from rest_framework import serializers
from ....models.models import Question, TipoMomento, Answer
from ..BaseSerializers import BaseSerializers
from ..momento.momento_serializers import MomentSerializers


class AswerSerialzersView(BaseSerializers):
    respuesta = serializers.CharField(read_only=True)


class QuestionSerializersView(BaseSerializers):
    pregunta_nombre = serializers.CharField(read_only=True)
    momento = MomentSerializers(read_only=True)
    tipo_pregunta = serializers.CharField(read_only=True)
    depende_respuesta = serializers.PrimaryKeyRelatedField(read_only=True)
    componente = serializers.CharField(read_only=True)

    answer_set = AswerSerialzersView(many=True)

    class Meta:
        fields = "__all__"


class QuestionSerializers(BaseSerializers):
    pregunta_nombre = serializers.CharField()
    momento = serializers.IntegerField()
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        momento = TipoMomento.objects.get(pk=validated_data["momento"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Question.objects.create(
            pregunta_nombre=validated_data["pregunta_nombre"],
            momento=momento,
            userCreate=userCreate,
        )

    def update(self, instance, validated_data):
        instance.pregunta_nombre = validated_data.get(
            "pregunta_nombre", instance.pregunta_nombre
        )
        instance.momento_id = validated_data.get("momento", instance.momento)

        instance.userUpdate = validated_data.get("userUpdate", instance.userUpdate)
        instance.visible = validated_data.get("visible", instance.visible)
        instance.save()
        return instance
