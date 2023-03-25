from rest_framework import serializers
<<<<<<< HEAD
from ....models.models import Categoria
from ..BaseSerializers import BaseSerializers

class CategorySerializers(BaseSerializers):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
=======
from ....models.models import Categoria,Seccion
from ..BaseSerializers import BaseSerializers


class CategorySerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
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
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
<<<<<<< HEAD
        
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Categoria.objects.create(name=validated_data["name"],userCreate=userCreate)
=======
        seccion = Seccion.objects.get(pk=validated_data["seccionId"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Categoria.objects.create(name=validated_data["name"],seccionId=seccion,userCreate=userCreate)
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance
