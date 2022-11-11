from rest_framework.generics import CreateAPIView
from ...serializers.resources.resources_serializers import ResourcesRolesSerializers
from ...serializers.roles.roles_serializers import RolesUserSerializers
from rest_framework import status
from ....models import Resources, User_roles
from rest_framework.response import Response
from ..modules import create_response


class SecurityResourcesCreate(CreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesRolesSerializers

    def post(self, request, *args, **kwargs):
        try:
            resources = ResourcesRolesSerializers(data=request.data)
            resources.is_valid(raise_exception=True)
            resources.create(request.data)
            response, code = create_response(
                status.HTTP_200_OK, 'Resources', 'Resources Create')
            return Response(response, code)
        except BaseException as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', e.args[0])
            return Response(response, status=code)


class SecurityRolesUser(CreateAPIView):
    queryset = User_roles.objects.all()
    serializer_class = RolesUserSerializers

    def post(self, request, *args, **kwargs):
        user = request.data['username']
        rol = request.data['rol']

        rolesUser = RolesUserSerializers(data={'userId': user, 'rolesId': rol})
        if rolesUser.is_valid():
            rolesUser.save()
            response, code = create_response(
                status.HTTP_200_OK, 'User-Rol', rolesUser.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', rolesUser.errors)
        return Response(response, status=code)
