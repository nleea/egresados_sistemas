from rest_framework import serializers
from ....models.models import Anuncio
from ..subCategory.subCategory_serializers import SubCategorySerializers
from apps.auth_module.api.serializers.user.users_serializers import UserSerializersSimple

class AdvertisementSerializers(serializers.Serializer):
    name = serializers.CharField()
    datos = serializers.CharField()
    categoriId = SubCategorySerializers()
    persona_id = UserSerializersSimple()
    
    class Meta:
        fields = "__all__"
    
    def create(self, validated_data):
        return Anuncio(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.datos = validated_data.get('datos', instance.datos)
        return instance