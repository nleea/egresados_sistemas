from rest_framework import serializers
from ....models.models import Anuncio,SubCategoria
from ..subCategory.subCategory_serializers import SubCategorySerializers
from apps.auth_module.api.serializers.user.users_serializers import UserSerializersSimple
from ..BaseSerializers import BaseSerializers

class AdvertisementSerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    datos = serializers.CharField()
    subCategori = serializers.SlugRelatedField("name",read_only=True)
    persona_id = serializers.SlugRelatedField("username",read_only=True)

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
        subCategory = SubCategoria.objects.get(pk=validated_data["subCategori"])
        userCreate = None
        if validated_data["persona_id"]:
            userCreate = validated_data["persona_id"]
        return Anuncio.objects.create(datos=validated_data["datos"],
                                      persona_id=userCreate,userCreate=userCreate,
                                      subCategori=subCategory)

    def update(self, instance, validated_data):
        try:
            if 'subCategori' in validated_data:
                subCategori = SubCategoria.objects.get(pk=validated_data["subCategori"])
                instance.subCategori = subCategori
            instance.datos = validated_data.get('datos', instance.datos)
            instance.save()
            return instance
        except(SubCategoria.DoesNotExist) as e:
            raise serializers.ValidationError(e.args[0])
        