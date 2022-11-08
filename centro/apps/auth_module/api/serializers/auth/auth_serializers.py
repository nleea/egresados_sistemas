from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from ..customValidators.usersValidators import UserValidatorBefore
from django.contrib.auth import login
from ...serializers.roles.roles_serializers import RolesSimpleSerializers
User = get_user_model()


class RegisterSerializers(serializers.ModelSerializer):

    username = serializers.SlugField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        validators = [UserValidatorBefore()]


class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(label='Email/username')
    password = serializers.CharField()
    roles = RolesSimpleSerializers(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'roles')

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            #login(self.context['request'], user)
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
