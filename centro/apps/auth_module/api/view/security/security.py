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
            return Response({'message': 'Ok'})
        except BaseException as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, e.args)
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
                status.HTTP_200_OK, rolesUser.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, rolesUser.errors)
        return Response(response, status=code)
