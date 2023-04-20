from rest_framework import serializers
from apps.auth_module.models import Headquarters, Faculties, Programs


class BaseSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    createdAt = serializers.DateField(read_only=True)
    updateAt = serializers.DateField(read_only=True)
    userCreate = serializers.SlugRelatedField("username",read_only=True)
    userUpdate = serializers.SlugRelatedField("username",read_only=True)
    
    
    def __init__(self, instance=None, data=..., **kwargs):
        meta = bool(kwargs.pop('meta', None))
        
        super().__init__(instance, data, **kwargs)
        
        if meta != True or meta is None:
            self.fields.pop("createdAt")
            self.fields.pop("updateAt")
            self.fields.pop("userCreate")
            self.fields.pop("userUpdate")
    

class HeadSerializers(BaseSerializers):
    name = serializers.CharField()
    
    
    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        head = Headquarters.objects.create(name=validated_data["name"])
        return head

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class FacultiesSerializers(BaseSerializers):
    name = serializers.CharField()
    sede = serializers.IntegerField(write_only=True)
    headquarter = serializers.SlugRelatedField("name", read_only=True)
    
    class Meta:
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            "id":instance.id,
            "name":instance.name,
            "sede": instance.headquarter.name
        }

    def create(self, validated_data):
        faculties = Faculties.objects.create(
            name=validated_data["name"], headquarter_id=validated_data["sede"])
        return faculties

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.headquarter_id = validated_data.get(
            "sede", instance.headquarter)
        instance.save()
        return instance


class ProgramsSerializers(BaseSerializers):
    name = serializers.CharField()
    faculta = serializers.IntegerField(write_only=True)
    faculty = serializers.SlugRelatedField("name", read_only=True)

    class Meta:
            fields = '__all__'

    def create(self, validated_data):
        faculties = Programs.objects.create(
            name=validated_data["name"], faculty_id=validated_data["faculta"])
        return faculties

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.faculty_id = validated_data.get(
            "faculta", instance.faculty)
        instance.save()
        return instance
