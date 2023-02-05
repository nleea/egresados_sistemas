from rest_framework import serializers
<<<<<<< HEAD
from ....models.models import Categoria,Seccion
from ..BaseSerializers import BaseSerializers

class CategorySerializers(BaseSerializers):
    name = serializers.CharField()
    seccionId = serializers.SlugRelatedField("name",read_only=True)
    
    def __init__(self, instance=None, data=..., **kwargs):
        meta = bool(kwargs.pop('meta', None))
        
        super().__init__(instance, data, **kwargs)
        
        if meta != True or meta is None:
            self.fields.pop("createdAt")
            self.fields.pop("updateAt")
            self.fields.pop("userCreate")
            self.fields.pop("userUpdate")
=======
from ..seccion.seccion_serializers import SeccionSerializers
from ....models.models import Categoria

class CategorySerializers(serializers.Serializer):
    name = serializers.CharField()
    seccionId = SeccionSerializers()
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
<<<<<<< HEAD
        seccion = Seccion.objects.get(pk=validated_data["seccionId"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Categoria.objects.create(name=validated_data["name"],seccionId=seccion,userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance
=======
        return Categoria(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
