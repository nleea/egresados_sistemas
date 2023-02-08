from rest_framework import serializers
from ....models.models import Pqrs,User
from ..BaseSerializers import BaseSerializers

class PqrsSerializers(BaseSerializers):
    description = serializers.CharField()
    persona = serializers.SlugRelatedField("username",read_only=True)

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
        persona = User.objects.get(pk=validated_data["persona"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return Pqrs.objects.create(description=validated_data["description"],persona=persona,userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
        instance.save()
        return instance
