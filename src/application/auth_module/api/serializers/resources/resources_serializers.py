from ....models import Resources, Resources_roles
from rest_framework.serializers import (
    Serializer,
    IntegerField,
    BooleanField,
    CharField,
    ListField,
)


class ResourcesSerializers(Serializer):
    id = IntegerField(read_only=True)
    path = CharField(read_only=True)
    id_padre = IntegerField(read_only=True)
    icono = CharField(read_only=True)
    link = CharField(read_only=True)
    titulo = CharField(read_only=True)

    class Meta:
        fields = "__All__"


class ResourcesCreateSerializers(Serializer):
    path = CharField()
    id_padre = IntegerField()
    link = CharField()
    titulo = CharField()
    icono = CharField(required=False)

    def create(self, validated_data):
        try:
            path = validated_data.get("path", None)
            id_padre = validated_data.get("id_padre", 0)
            link = validated_data.get("link", None)
            titulo = validated_data.get("titulo", None)
            icono = validated_data.get("icono", "icon")

            instance = Resources.objects.create(
                pk=Resources.objects.last().pk + 1,
                path=path,
                id_padre=id_padre,
                link=link,
                titulo=titulo,
                method="GET",
                icono=icono,
            )
            return instance
        except Exception as e:
            raise e

    class Meta:
        fields = "__all__"


class ResourcesRolesSerializers(Serializer):
    merge = BooleanField(required=False)
    rolesId = IntegerField()
    resources = ListField(child=IntegerField())

    def create(self, validated_data):
        try:
            
            list_resources_roles = [
                Resources_roles(
                    rolesId_id=validated_data["rolesId"], resourcesId_id=resource
                )
                for resource in validated_data.get("resources", [])
            ]

            instane = Resources_roles.objects.bulk_create(list_resources_roles)[0]
            return instane
        except Exception as e:
            raise e
