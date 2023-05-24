from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from ...serializers.resources.resources_serializers import ResourcesRolesSerializers
from rest_framework import status
from ....models import Resources,User
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


class SecurityRolesUser(APIView):

    def post(self, request, *args, **kwargs):
        user = request.data['user']
        rolesId = request.data['roles']
        roles = Group.objects.filter(id__in=rolesId)
        
        try:
            if roles:
                User.objects.get(pk=user).groups.set([x.pk for x in roles])
            return Response("Success",  status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args,  status.HTTP_400_BAD_REQUEST)


class CheckPermissions(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        permissions = request.data["permissions"]

        checkResulst = user.has_perms(permissions)

        return Response({"valid":checkResulst},status=status.HTTP_200_OK)
