from ....models import Roles
from rest_framework.serializers import ModelSerializer


class RolesSerializers(ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name', 'status')


class RolesSimpleSerializers(ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name', 'status')
