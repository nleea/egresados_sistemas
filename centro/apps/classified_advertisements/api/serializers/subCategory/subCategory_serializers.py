from rest_framework import serializers
from ..category.category_serializers import CategorySerializers
from ....models.models import SubCategoria

class SubCategorySerializers(serializers.Serializer):
    name = serializers.CharField()
    categoriId = CategorySerializers()
    
    class Meta:
        fields = "__all__"
    
    def create(self, validated_data):
        return SubCategoria(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance