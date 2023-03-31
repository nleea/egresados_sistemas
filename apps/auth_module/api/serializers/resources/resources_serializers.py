from ....models import Resources, Resources_roles, Roles
from rest_framework.serializers import ModelSerializer, Serializer, IntegerField
from .....helpers.menu_resources import menuResources


class ResourcesSerializers(ModelSerializer):
    class Meta:
        model = Resources
        exclude = ('roles',)


class ResourcesRolesSerializers(Serializer):
    rolesId = IntegerField()
    resources = ResourcesSerializers(many=True)

    def create(self, validated_data):
        try:
            resources = []
            list_resources_roles = []

            id_last_resources = 0
            last = Resources.objects.last()
            
            # for i in validated_data["resources"]:
            #     if "id_padre" in i:
                    
            if last:
                id_last_resources = last.id + 1 # type: ignore

            menuResources(validated_data['resources'],
                          resources, Resources, id_last_resources)
            
            
            resources = Resources.objects.bulk_create(resources)

            roles = Roles.objects.get(pk=validated_data['rolesId'])

            list_resources_roles = [Resources_roles(
                rolesId=roles, resourcesId=r) for r in resources]

            Resources_roles.objects.bulk_create(list_resources_roles)
            return None
        except Exception as e:
            raise e
