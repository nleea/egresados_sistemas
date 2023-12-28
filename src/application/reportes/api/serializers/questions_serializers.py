from rest_framework import serializers


from src.application.auth_module.api.serializers.user.users_serializers import (
    UserSerializersSimple,
)

from src.application.default.base_serializer import BaseSerializers

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


class AswerSerialzersViewa(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    respuesta = serializers.CharField(read_only=True)
    pregunta = serializers.SlugRelatedField("pk", read_only=True)
    
    

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["pregunta_id"] = instance.pregunta.pk

        return data

    class Meta:
        fields = "__all__"


class ReporteSerializersViewa(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    repuesta = serializers.SlugRelatedField("pk", read_only=True)
    pregunta = serializers.SlugRelatedField("pk", read_only=True)
    user = serializers.SlugRelatedField("pk", read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["respuesta_id"] = instance.respuesta.pk
        data["pregunta_id"] = instance.pregunta.pk
        data["user_id"] = instance.user.pk

        return data

    class Meta:
        fields = "__all__"


class QuestionSerializersViewda(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    pregunta_nombre = serializers.CharField(read_only=True)

    class Meta:
        fields = "__all__"
