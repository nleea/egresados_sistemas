from ..roles.roles_serializers import RolesSerializers
from rest_framework.serializers import CharField, ModelSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

#from drf_queryfields import QueryFieldsMixin


class UserSerializersSimple(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserSerializers(ModelSerializer):
    roles = RolesSerializers(many=True, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            if (len(representation['roles'])):
                representation['roles'][0] = representation['roles'][0]['id']
            return representation
        except Exception as e:
            return representation

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'roles')


class CreateUserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserSerializersSimpleRegister(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class UserChangePassword(ModelSerializer):
    password = CharField()

    class Meta:
        model = User
        fields = ('password',)
