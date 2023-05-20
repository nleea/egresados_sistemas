from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from ...serializers.resources.resources_serializers import ResourcesRolesSerializers
from ...serializers.roles.roles_serializers import RolesUserSerializers
from rest_framework import status
from ....models import Resources, User_roles
from rest_framework.response import Response
from django.contrib.auth.models import Group

class SecurityResourcesCreate(CreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesRolesSerializers

    def post(self, request, *args, **kwargs):
        try:
            resources = ResourcesRolesSerializers(data=request.data)
            resources.is_valid(raise_exception=True)
            resources.create(request.data)
            return Response('Resources Create', status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


class SecurityRolesUser(CreateAPIView):
    queryset = User_roles.objects.all()
    serializer_class = RolesUserSerializers

    def post(self, request, *args, **kwargs):
        user = request.data['user']
        rolesId = request.data['roles']
        roles = Group.objects.filter(id__in=rolesId)

        rolesUser = RolesUserSerializers(
            data={'userId': user})  # type: ignore

        if rolesUser.is_valid():
            rolesUser.save(roles=roles)
            return Response('successfully assigned roles', status.HTTP_200_OK)
        return Response(rolesUser.errors,  status.HTTP_400_BAD_REQUEST)


class CheckPermissions(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        permissions = request.data["permissions"]

        checkResulst = user.has_perms(permissions)

        return Response({"valid":checkResulst},status=status.HTTP_200_OK)
