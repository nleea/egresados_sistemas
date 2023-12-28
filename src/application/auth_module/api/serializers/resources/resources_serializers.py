from ....models import Resources, Resources_roles
from rest_framework.serializers import Serializer, IntegerField, BooleanField, CharField
from configs.helpers.menu_resources import menuResources


class ResourcesSerializers(Serializer):
    id = IntegerField(read_only=True)
    path = CharField(read_only=True)
    id_padre = IntegerField(read_only=True)
    path = CharField(read_only=True)
    icono = CharField(read_only=True)
    link = CharField(read_only=True)
    titulo = CharField(read_only=True)

    class Meta:
        fields = "__All__"


class ResourcesRolesSerializers(Serializer):
    merge = BooleanField(required=False)
    rolesId = IntegerField()
    resources = ResourcesSerializers(many=True)

    def create(self, validated_data):
        try:
            merge = validated_data.get("merge",False)
            new_resources = []
            resources = []
            list_resources_roles = []

            id_last_resources = 0
            last = Resources.objects.last()

            if merge:
                for _, resource in enumerate(validated_data["resources"]):
                    id_padre = Resources.objects.get(path=resource["path"]).pk
                    new_resources = [{**x, "id_padre": id_padre}
                                     for x in resource["items"]]

            if last:
                id_last_resources = last.id + 1  # type: ignore

            menuResources(new_resources if merge else validated_data["resources"],
                          resources, Resources, id_last_resources)

            resources = Resources.objects.bulk_create(resources)

            list_resources_roles = [Resources_roles(
                rolesId_id=validated_data['rolesId'], resourcesId=resource) for resource in resources]

            Resources_roles.objects.bulk_create(list_resources_roles)
            return None
        except Exception as e:
            raise e
