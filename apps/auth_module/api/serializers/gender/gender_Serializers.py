
from rest_framework import serializers


class GenderSerializersView(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        fields = "__all__"


class GenderSerializers(serializers.Serializer):
    name = serializers.CharField()

    class Meta:
        fields = "__all__"
