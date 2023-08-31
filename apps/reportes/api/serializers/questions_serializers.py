from rest_framework import serializers
from apps.encuestas.models.models import Question
from .BaseSerializers import BaseSerializers

from apps.encuestas.api.serializers.questions.questions_serializers import (
    QuestionRSerializersView,
)

from apps.auth_module.api.serializers.user.users_serializers import (
    UserSerializersSimple,
)


class AswerUserSerializers(BaseSerializers):
    # respuesta = serializers.IntegerField()
    # texto = serializers.CharField()
    user = UserSerializersSimple()


class AswerSerialzersView(BaseSerializers):
    respuesta = serializers.CharField(read_only=True)
    count_user = serializers.IntegerField(read_only=True)


class QuestionSerializersViewd(BaseSerializers):
    pregunta_nombre = serializers.CharField(read_only=True)
    tipo_pregunta = serializers.CharField(
        read_only=True, source="get_tipo_pregunta_display"
    )
    total_respuestas = serializers.IntegerField(read_only=True)

    answer_set = AswerSerialzersView(many=True)
    # answeruser_set = AswerUserSerializers(many=True)

    class Meta:
        fields = "__all__"


class QuestionSerializersView(BaseSerializers):
    pregunta_nombre = serializers.CharField(read_only=True)
    tipo_pregunta = serializers.CharField(
        read_only=True, source="get_tipo_pregunta_display"
    )
    componente = serializers.CharField(read_only=True)


class ReporteSerializersView(BaseSerializers):
    repuesta = QuestionSerializersView(read_only=True)
    respuesta = AswerSerialzersView(read_only=True)
    texto = serializers.CharField(read_only=True)
    num = serializers.IntegerField(read_only=True)

    class Meta:
        fields = "__all__"
