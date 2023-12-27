from ....models import User
from rest_framework import serializers
from django.contrib.auth.models import Group


class UserSerilizers(serializers.Serializer):
    class Meta:
        fields = "__all__"


class RolesSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            return Group.objects.create(**validated_data)
        except Exception as e:
            return e.args

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


# class RolesUserSerializers(ModelSerializer):
#     class Meta:
#         model = User_roles
#         exclude = ('rolesId',)

#     def create(self, validated_data):
#         user = validated_data['userId']
#         rolesForUser = [User_roles(
#             userId=user, rolesId=x) for x in validated_data['roles']]

#         try:
#             response = User_roles.objects.bulk_create(rolesForUser)
#             return response[0]
#         except Exception as e:
#             raise ValidationError('Duplicate Key User - Rol', 404)
