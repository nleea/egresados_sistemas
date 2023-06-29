from rest_framework import serializers
from ....models.models import Question, TipoMomento, Answer
from ..BaseSerializers import BaseSerializers
from ..momento.momento_serializers import MomentSerializers
from django.db import transaction

class AswerSerialzersView(BaseSerializers):
    respuesta = serializers.CharField(read_only=True)


class QuestionSerializersViewDepende(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)


class AswerSerialzersViewDepende(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    pregunta = QuestionSerializersViewDepende(read_only=True)


class QuestionSerializersView(BaseSerializers):
    pregunta_nombre = serializers.CharField(read_only=True)
    momento = MomentSerializers(read_only=True)
    tipo_pregunta = serializers.CharField(read_only=True)
    depende_respuesta = AswerSerialzersViewDepende(read_only=True)
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


class AswerUserSerializers(BaseSerializers):
    respuesta = serializers.IntegerField()
    texto = serializers.CharField()
    user = serializers.IntegerField()

    def create(self, validated_data):
        return super().create(validated_data)


class QuestionCreateSerializers(BaseSerializers):
    question = serializers.CharField()
    depend = serializers.IntegerField(required=False,allow_null=True)
    type = serializers.CharField()
    options = serializers.ListField(required=False)
    momento = serializers.IntegerField()

    def create(self, validated_data):
        try:
            with transaction.atomic():
                pregunta = Question.objects.create(
                pregunta_nombre=validated_data["question"],
                momento_id=validated_data["momento"],
                tipo_pregunta=validated_data["type"].lower(),
                depende_respuesta_id=validated_data["depend"]
                if "depend" in validated_data
                else None,
                userCreate=validated_data["userCreate"]
            )
                if validated_data["options"]:
                    answers = []
                    options = validated_data["options"]

                    for i in options:
                        answers.append(Answer(respuesta=i["answer"], pregunta_id=pregunta.pk,userCreate=validated_data["userCreate"]))

                    Answer.objects.bulk_create(answers)
                return pregunta
        except Exception as e:
            transaction.rollback()
            raise serializers.ValidationError(e.args)
