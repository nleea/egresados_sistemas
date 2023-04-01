from ....models import Resources, Resources_roles, Roles
from rest_framework.serializers import ModelSerializer, Serializer, IntegerField, BooleanField
from .....helpers.menu_resources import menuResources


class ResourcesSerializers(ModelSerializer):
    class Meta:
        model = Resources
        exclude = ('roles',)


class ResourcesRolesSerializers(Serializer):
    merge = BooleanField()
    rolesId = IntegerField()
    resources = ResourcesSerializers(many=True)

    def create(self, validated_data):
        try:
            new_resources = []
            resources = []
            list_resources_roles = []

            id_last_resources = 0
            last = Resources.objects.last()

            if validated_data["merge"] == True:
                for i in validated_data["resources"]:
                    id_padre = Resources.objects.filter(path=i["path"])[0].pk
                    new_resources = [{**x, "id_padre": id_padre}
                                     for x in i["items"]]

            if last:
                id_last_resources = last.id + 1  # type: ignore

            menuResources(new_resources if validated_data["merge"] else validated_data["resources"],
                          resources, Resources, id_last_resources)

            resources = Resources.objects.bulk_create(resources)

            roles = Roles.objects.get(pk=validated_data['rolesId'])

            list_resources_roles = [Resources_roles(
                rolesId=roles, resourcesId=r) for r in resources]

            Resources_roles.objects.bulk_create(list_resources_roles)
            return None
        except Exception as e:
            raise e