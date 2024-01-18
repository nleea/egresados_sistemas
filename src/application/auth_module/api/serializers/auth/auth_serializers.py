from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import Group
from rest_framework.validators import UniqueValidator
from ..customValidators.usersValidators import UserValidatorBefore
from src.application.auth_module.models import User, Persons
from ...serializers.person.persons_serializers import (
    PersonsSimpleSerializersView,
    PersonsSerializer,
)
from django.db import transaction

User = get_user_model()


class RegisterSerializers(serializers.Serializer):
    username = serializers.SlugField(
        max_length=100, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField()
    password = serializers.CharField()
    persona = PersonsSerializer(write_only=True)

    class Meta:
        fields = "__all__"
        validators = [UserValidatorBefore()]

    def create(self, validated_data):
        try:
            with transaction.atomic():
                persona = validated_data.pop("persona", None)
                rol = validated_data.pop("rol", None)
                user = User.objects.create(**validated_data, is_staff=True)
                document_type = persona.pop("document_type", None)
                gender_type = persona.pop("gender_type", None)

                Persons.objects.create(
                    **persona,
                    document_type_id=document_type,
                    gender_type_id=gender_type,
                    user=user
                )

                if rol == None:
                    group_egresado = Group.objects.get(pk=2)
                    user.groups.add(group_egresado)  # type:ignore
                else:
                    group_selected = Group.objects.get(pk=rol)
                    user.groups.add(group_selected)  # type:ignore
            return user
        except Exception as e:
            transaction.rollback()
            return e


class LoginSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(label="Email/username")
    password = serializers.CharField()
    person = PersonsSimpleSerializersView(read_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials Passed.")
