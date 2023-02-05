from rest_framework import serializers
<<<<<<< HEAD
from ....models.models import SubCategoria,Categoria
from ..BaseSerializers import BaseSerializers

class SubCategorySerializers(BaseSerializers):
    name = serializers.CharField()
    categoriId = serializers.SlugRelatedField('name',read_only=True)

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
        category = Categoria.objects.get(pk=validated_data["categoryId"])
        userCreate = None
        if validated_data["userCreate"]:
            userCreate = validated_data["userCreate"]
        return SubCategoria.objects.create(name=validated_data["name"],categoriId=category,userCreate=userCreate)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.userUpdate = validated_data.get('userUpdate', instance.userUpdate)
        instance.save()
=======
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
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
        return instance