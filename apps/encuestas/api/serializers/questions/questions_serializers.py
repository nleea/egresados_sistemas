from rest_framework import serializers
from ....models.models import Question,TipoMomento
from ..BaseSerializers import BaseSerializers

class QuestionSerializers(BaseSerializers):
    pregunta_nombre = serializers.CharField()
    momento = serializers.SlugRelatedField("tipo",read_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        momento = TipoMomento.objects.get(pk=validated_data["momento"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Question.objects.create(pregunta_nombre=validated_data["pregunta_nombre"],momento=momento,userCreate=userCreate)

    def update(self, instance, validated_data):

        instance.pregunta_nombre = validated_data.get('pregunta_nombre', instance.pregunta_nombre)
        if "momento" in validated_data:
            try:
                momento = TipoMomento.objects.get(pk=validated_data["momento"])
                instance.momento = momento
            except TipoMomento.DoesNotExist as e:
                raise serializers.ValidationError(e)

        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance


class QuestionSerializersUpate(BaseSerializers):
    pregunta_nombre = serializers.CharField()
    momento = serializers.IntegerField()

    class Meta:
        fields = "__all__"

    def update(self, instance, validated_data):

        instance.pregunta_nombre = validated_data.get('pregunta_nombre', instance.pregunta_nombre)
        if "momento" in validated_data:
            try:
                momento = TipoMomento.objects.get(pk=validated_data["momento"])
                instance.momento = momento
            except TipoMomento.DoesNotExist as e:
                raise serializers.ValidationError(e)

        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance
