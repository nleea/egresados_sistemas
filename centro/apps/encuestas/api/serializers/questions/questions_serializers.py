from rest_framework import serializers
from ....models.models import Question,TipoMomento
from ..BaseSerializers import BaseSerializers

class QuestionSerializers(BaseSerializers):
    pregunta_nombre = serializers.CharField()
    momento = serializers.SlugRelatedField("tipo",read_only=True)

    def __init__(self, instance=None, data=..., **kwargs):
        meta = bool(kwargs.pop('meta', None))
        
        super().__init__(instance, data, **kwargs)
        
        if meta != True or meta is None:
            self.fields.pop("createdAt")
            self.fields.pop("updateAt")
            self.fields.pop("userCreate")
            self.fields.pop("userUpdate")

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
        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance
