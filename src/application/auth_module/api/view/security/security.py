import json
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
from django.contrib.contenttypes.models import ContentType


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
        contentypes = ContentType.objects.all()

        all_contentypes = {}
        for content in contentypes:
            
            
            if content.app_label in ["admin", "auth", "contenttypes", "sessions", "authtoken", "token_blacklist"]:
                continue
            
            if content.app_label not in all_contentypes:
                all_contentypes[content.app_label] = {}

            all_contentypes[content.app_label][content.model] = [
                x.name
                for x in Permission.objects.filter(content_type__model=content.model)
            ]

        return Response({"Message": all_contentypes}, status=status.HTTP_200_OK)


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
