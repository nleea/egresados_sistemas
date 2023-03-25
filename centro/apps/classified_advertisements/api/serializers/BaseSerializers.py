from rest_framework import serializers

class BaseSerializers(serializers.Serializer):
    
    createdAt = serializers.DateField(read_only=True)
    updateAt = serializers.DateField(read_only=True)
    userCreate = serializers.SlugRelatedField("username",read_only=True)
    userUpdate = serializers.SlugRelatedField("username",read_only=True)
    
<<<<<<< HEAD
    
    def __init__(self, instance=None, data=..., **kwargs):
        meta = bool(kwargs.pop('meta', None))
        
        super().__init__(instance, data, **kwargs)
        
        if meta != True or meta is None:
            self.fields.pop("createdAt")
            self.fields.pop("updateAt")
            self.fields.pop("userCreate")
            self.fields.pop("userUpdate")
    
=======
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345

