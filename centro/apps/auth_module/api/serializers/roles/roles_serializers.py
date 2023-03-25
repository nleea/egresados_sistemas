from ....models import Roles, User_roles, Resources_roles, User
from rest_framework.serializers import ModelSerializer, ValidationError
from .....helpers.create_response import create_response


class UserSerilizers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RolesSerializers(ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name')


class ResourcesSerializers(ModelSerializer):
    class Meta:
        model = Resources_roles
        fields = '__all__'


class RolesSimpleSerializers(ModelSerializer):
    resources = ResourcesSerializers(many=True)

    class Meta:
        model = User_roles
        fields = '__all__'


class RolesUserSerializers(ModelSerializer):
    class Meta:
        model = User_roles
        exclude = ('rolesId',)

    def create(self, validated_data):
        user = validated_data['userId']
        rolesForUser = [User_roles(
            userId=user, rolesId=x) for x in validated_data['roles']]

        try:
            response = User_roles.objects.bulk_create(rolesForUser)
            return response[0]
        except Exception as e:
            response, code = create_response(
                404, '', 'Duplicate Key User - Rol')
            raise ValidationError(response, code=code)
