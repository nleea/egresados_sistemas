from rest_framework import serializers
from ....models.models import SubCategoria,Categoria
from ..BaseSerializers import BaseSerializers
from ...serializers.category.category_serializers import CategorySerializers

class SubCategorySerializersView(BaseSerializers):
    id = serializers.IntegerField()
    name = serializers.CharField()
    categoriId = serializers.PrimaryKeyRelatedField(read_only=True)


class SubCategorySerializers(BaseSerializers):
    name = serializers.CharField()
    categoriId = serializers.CharField()
        

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return SubCategoria.objects.create(name=validated_data["name"],categoriId_id=validated_data["categoriId"],userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.categoriId_id = validated_data.get("categoriId",instance.categoriId)
        instance.userUpdate = validated_data.get('userUpdate', instance.userUpdate)
        instance.save()
        return instance