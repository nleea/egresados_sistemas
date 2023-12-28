from rest_framework import serializers
from ....models.models import SubCategoria
from ...serializers.category.category_serializers import CategorySerializers
from src.application.default.base_serializer import BaseSerializers


class SubCategorySerializersView(BaseSerializers):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    categoriaId = CategorySerializers(read_only=True)


class SubCategorySerializers(BaseSerializers):
    name = serializers.CharField()
    categoriaId = serializers.CharField()
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        model = SubCategoria
        fields = "__all__"

    def create(self, validated_data):
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return SubCategoria.objects.create(
            name=validated_data["name"],
            categoriaId_id=validated_data["categoriaId"],
            userCreate=userCreate,
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.categoriaId_id = validated_data.get(
            "categoriaId", instance.categoriaId
        )
        instance.userUpdate = validated_data.get("userUpdate", instance.userUpdate)
        instance.visible = validated_data.get("visible", instance.visible)

        instance.save()
        return instance
