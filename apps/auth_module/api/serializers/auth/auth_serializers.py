from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from ..customValidators.usersValidators import UserValidatorBefore
from ....models import Persons, User
from ...serializers.roles.roles_serializers import RolesSimpleSerializers
from ...serializers.person.persons_serializers import PersonsSimpleSerializers
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
        fields = '__all__'
        validators = [UserValidatorBefore()]

    person = PersonsSimpleSerializers(read_only=True)


    def create(self, validated_data):
        #person = validated_data.pop('person')
        user = User.objects.create(**validated_data)
        #Persons.objects.create(**person, user=user)
        return user


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
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
