from ....models import Roles, User_roles, Resources_roles
from rest_framework.serializers import ModelSerializer


class RolesSerializers(ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name', 'status')


class ResourcesSerializers(ModelSerializer):
    class Meta:
        model = Resources_roles
        fields = '__al__'


class RolesSimpleSerializers(ModelSerializer):
    resources = ResourcesSerializers(many=True)

    class Meta:
        model = User_roles
        fields = '__all__'
