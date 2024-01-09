from ..roles.roles_serializers import RolesSerializers
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from ..customValidators.usersValidators import UserValidatorBefore

User = get_user_model()


class UserSerializersSimple(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        fields = ("username", "email")

    def __init__(self, instance=None, data=..., **kwargs):
        expands = kwargs.pop("expands", True)
        meta = kwargs.pop("meta", False)
        super().__init__(instance, data, **kwargs)

        if not expands:
            self.fields.pop("username")


class UserSerializers(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    groups = RolesSerializers(read_only=True, many=True)

    class Meta:
        fields = "__all__"


class CreateUserSerializers(serializers.ModelSerializer):
    username = serializers.SlugField(
        max_length=100, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ("username", "password", "email")
        validators = [UserValidatorBefore()]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create(**validated_data)


class UserSerializersSimpleRegister(serializers.ModelSerializer):
    username = serializers.SlugField(
        max_length=100, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        validators = [UserValidatorBefore()]


class UserChangePassword(serializers.Serializer):
    password = serializers.CharField()
    original_password = serializers.CharField()

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.password = validated_data.get("password", instance.password)

        return instance
