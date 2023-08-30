from rest_framework import serializers
from apps.encuestas.models.models import Question
from .BaseSerializers import BaseSerializers

from apps.encuestas.api.serializers.questions.questions_serializers import (
    QuestionSerializersView,
    QuestionRSerializersView,
    AswerUserSerializers,
)


class ReporteSerializersView(BaseSerializers):
    pregunta_nombre = serializers.CharField(read_only=True)
    tipo_pregunta = serializers.CharField(
        read_only=True, source="get_tipo_pregunta_display"
    )

    facultad = serializers.CharField(read_only=True)
    num = serializers.IntegerField(read_only=True)
    promedio_respuestas = serializers.FloatField(read_only=True)

    class Meta:
        fields = "__all__"
