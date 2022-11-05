from ....models import Resources, Resources_roles, Roles
from rest_framework.serializers import ModelSerializer, Serializer, IntegerField


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

            id_last_resources = Resources.objects.last().id

            for i in validated_data['resources']:
                resources.append(Resources(
                    path=i['path'], link=i['link'], icono=i['icono'], method=i['method'], titulo=i['titulo'], id_padre=i['id_padre'], id=id_last_resources+1))
                id_last_resources += 1

            resources = Resources.objects.bulk_create(resources)

            roles = Roles.objects.get(pk=validated_data['rolesId'])

            for r in resources:
                list_resources_roles.append(Resources_roles(
                    rolesId=roles, resourcesId=r))

            Resources_roles.objects.bulk_create(list_resources_roles)
            return None
        except Exception as e:
            raise e
