from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.models import Group
from rest_framework.validators import UniqueValidator
from ..customValidators.usersValidators import UserValidatorBefore
from ....models import User,Persons
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

    persona = PersonsSimpleSerializers()


    def create(self, validated_data):
        persona = validated_data.pop('persona')
        rol = validated_data.pop("rol",None)
        user = User.objects.create(**validated_data)
        Persons.objects.create(**persona, user=user)

        if rol == None:
            group_egresado= Group.objects.get(pk=2)
            user.groups.add(group_egresado)#type:ignore
        else:
            group_selected = Group.objects.get(pk=rol)
            user.groups.add(group_selected)#type:ignore
        return user


class LoginSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(label='Email/username')
    password = serializers.CharField()
    roles = serializers.ListField(required=False,read_only=True)
    person = PersonsSimpleSerializers(read_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
