from rest_framework import serializers

class BaseSerializers(serializers.Serializer):
    
    createdAt = serializers.DateField(read_only=True)
    updateAt = serializers.DateField(read_only=True)
    userCreate = serializers.SlugRelatedField("username",read_only=True)
    userUpdate = serializers.SlugRelatedField("username",read_only=True)
    

