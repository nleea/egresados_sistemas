from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from ....models import Roles
from ...serializers.roles.roles_serializers import RolesSerializers
from ..modules import (CreateAPIView, ListAPIView, Response, UpdateAPIView,
                       create_response, status)


class RolesListView(ListAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = RolesSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'Roles', serializers.data)
        return Response(response, status=code)


class RolescreateView(CreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def post(self, request, *args, **kwargs):
        roleSerializers = RolesSerializers(data=request.data)
        if roleSerializers.is_valid():
            roleSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Role', roleSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_200_OK, 'Error', roleSerializers.error)
        return Response(response, status=code)


class RoleUpdateView(UpdateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Roles.objects.get(pk)
        except Roles.DoesNotExist:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Role Not Found', 'Not Found')
            return {'response': response, 'code': code}

    def put(self, request, *args, **kwargs):
        role = self.get_object()
        if type(role) is dict:
            return Response(role['response'], role['code'])
        roleSerializers = RolesSerializers(role, data=request.data)
        if roleSerializers.is_valid():
            roleSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Role', roleSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_200_OK, 'Error', roleSerializers.errors)
        return Response(response, status=code)
