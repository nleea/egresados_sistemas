from rest_framework import serializers
from ....models.models import SubCategoria,Categoria
from ..BaseSerializers import BaseSerializers
from ..category.category_serializers import CategorySerializers

class SubCategorySerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    categoriId = CategorySerializers(read_only=True)
        

    class Meta:
        model = SubCategoria
        fields = "__all__"

    def create(self, validated_data):
        category = Categoria.objects.get(pk=validated_data["categoryId"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return SubCategoria.objects.create(name=validated_data["name"],categoriId=category,userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.userUpdate = validated_data.get('userUpdate', instance.userUpdate)
        instance.save()
        return instance