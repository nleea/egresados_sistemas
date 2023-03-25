from rest_framework import serializers
from ....models.models import SubCategoria,Categoria
from ..BaseSerializers import BaseSerializers
<<<<<<< HEAD
from ...serializers.category.category_serializers import CategorySerializers

class SubCategorySerializersView(BaseSerializers):
    id = serializers.IntegerField()
    name = serializers.CharField()
    categoriId = serializers.PrimaryKeyRelatedField(read_only=True)


class SubCategorySerializers(BaseSerializers):
    name = serializers.CharField()
    categoriId = serializers.CharField()
=======
from ..category.category_serializers import CategorySerializers

class SubCategorySerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    categoriId = CategorySerializers(read_only=True)
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345
        

    class Meta:
        model = SubCategoria
        fields = "__all__"

    def create(self, validated_data):
<<<<<<< HEAD
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return SubCategoria.objects.create(name=validated_data["name"],categoriId_id=validated_data["categoriId"],userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.categoriId_id = validated_data.get("categoriId",instance.categoriId)
=======
        category = Categoria.objects.get(pk=validated_data["categoryId"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return SubCategoria.objects.create(name=validated_data["name"],categoriId=category,userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345
        instance.userUpdate = validated_data.get('userUpdate', instance.userUpdate)
        instance.save()
        return instance