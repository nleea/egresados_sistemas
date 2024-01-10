from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from ...serializers.resources.resources_serializers import (
    ResourcesRolesSerializers,
    ResourcesSerializers,
)
from rest_framework import status
from ....models import Resources, User
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class SecurityResourcesCreate(CreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesRolesSerializers

    def post(self, request, *args, **kwargs):
        try:
            resources = ResourcesRolesSerializers(data=request.data)
            resources.is_valid(raise_exception=True)
            resources.create(request.data)
            return Response("Resources Create", status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class SecurityRolesUser(APIView):
    def post(self, request, *args, **kwargs):
        user = request.data["user"]
        roles_id = request.data["roles"]
        roles = Group.objects.filter(id__in=roles_id)

        try:
            if roles:
                User.objects.get(pk=user).groups.set([x.pk for x in roles])
            return Response("Success", status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class PermissionsView(APIView):
    def get(self, request, *args, **kwargs):
        permission = Permission.objects.all()

        print(permission)

        return Response({"Message": "Ok"}, status=status.HTTP_200_OK)


class CheckPermissions(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        permissions = request.data["permissions"]

        check_resulst = user.has_perms(permissions)

        return Response({"valid": check_resulst}, status=status.HTTP_200_OK)


class ResourcesView(APIView):
    def get(self, request, *args, **kwargs):
        resources = Resources.objects.all()
        serializer = ResourcesSerializers(resources, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
