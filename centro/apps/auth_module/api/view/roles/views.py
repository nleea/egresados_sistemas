from ..modules import CreateAPIView, ListAPIView, Response, UpdateAPIView, status, create_response
from ....models import Roles
from ...serializers.roles.roles_serializers import RolesSerializers


class RolesListView(ListAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = RolesSerializers(data, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class RolescreateView(CreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def post(self, request, *args, **kwargs):
        roleSerializers = RolesSerializers(data=request.data)
        if roleSerializers.is_valid():
            roleSerializers.save()
            return Response(roleSerializers.data, status=status.HTTP_200_OK)
        return Response(roleSerializers.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleUpdateView(UpdateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Roles.objects.get(pk)
        except Roles.DoesNotExist:
            raise Response(
                create_response(
                    "", status.HTTP_400_BAD_REQUEST, {'message': 'Not Found'})
            )

    def put(self, request, *args, **kwargs):
        role = self.get_object()
        roleSerializers = RolesSerializers(role, data=request.data)
        if roleSerializers.is_valid():
            roleSerializers.save()
            return Response(roleSerializers.data, status=status.HTTP_200_OK)
        return Response(roleSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
