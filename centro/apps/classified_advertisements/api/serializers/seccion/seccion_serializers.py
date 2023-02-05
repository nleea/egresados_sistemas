from rest_framework import serializers
from ....models.models import Seccion
from ..BaseSerializers import BaseSerializers

class SeccionSerializers(BaseSerializers):
    name = serializers.CharField()
    
    def __init__(self, instance=None, data=..., **kwargs):
        meta = bool(kwargs.pop('meta', None))
        
        super().__init__(instance, data, **kwargs)
        
        if meta != True or meta is None:
            self.fields.pop("createdAt")
            self.fields.pop("updateAt")
            self.fields.pop("userCreate")
            self.fields.pop("userUpdate")

    class Meta:
        fields = ["name"]
        read_only_fields = ['createdAt','updateAt']

    def create(self, validated_data):
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Seccion.objects.create(name=validated_data["name"],userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.userUpdate = validated_data.get('userUpdate', instance.userUpdate)
        instance.save()
        return instance
    