from rest_framework import serializers


class BaseSerializers(serializers.Serializer):
    createdAt = serializers.DateField(read_only=True)
    updateAt = serializers.DateField(read_only=True)
    userCreate = serializers.CharField(read_only=True)
    userUpdate = serializers.CharField(read_only=True)

    def __init__(self, instance=None, data=..., **kwargs):
        meta = bool(kwargs.pop("meta", None))
        excludes = list(kwargs.pop("excludes", []))

        for i in excludes:
            self.fields.pop(i)

        super().__init__(instance, data, **kwargs)

        if meta != True or meta is None:
            self.fields.pop("createdAt")
            self.fields.pop("updateAt")
            self.fields.pop("userCreate")
            self.fields.pop("userUpdate")
