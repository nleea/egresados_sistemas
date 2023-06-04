from ...serializers.roles.roles_serializers import RolesSerializers
from ..modules import (CreateAPIView, Response,status)
from rest_framework.views import APIView
from django.contrib.auth.models import Group

class RolesListView(APIView):

    def get(self, request, *args, **kwargs):
        data = Group.objects.all()
        serializers = RolesSerializers(data, many=True)
        return Response(serializers.data, status.HTTP_200_OK)


class RolescreateView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = RolesSerializers

    def post(self, request, *args, **kwargs):
        roleSerializers = RolesSerializers(data=request.data)

        if roleSerializers.is_valid():
            roleSerializers.save()
            return Response(roleSerializers.data, status.HTTP_200_OK)
        return Response(roleSerializers.errors, status.HTTP_400_BAD_REQUEST)


# class RoleUpdateView(UpdateAPIView):
#     queryset = Roles.objects.all()
#     serializer_class = RolesSerializers

#     def get_object(self):
#         try:
#             pk = self.kwargs.get('pk')
#             return Roles.objects.get(id=pk)
#         except Roles.DoesNotExist:
#             return None

#     def put(self, request, *args, **kwargs):
#         role = self.get_object()
#         if role is None:
#             return Response('Role Not Exist', status.HTTP_200_OK)

#         try:
#             roleSerializers = RolesSerializers(role, data=request.data)
#             if roleSerializers.is_valid():
#                 roleSerializers.save()
#                 return Response(roleSerializers.data, status.HTTP_200_OK)
#             return Response(roleSerializers.errors, status.HTTP_200_OK)
#         except (AttributeError, Exception) as e:
#             return Response(e.args, status.HTTP_400_BAD_REQUEST)


# class RolesDestroyView(DestroyAPIView):
#     queryset = Roles.objects.all()
#     serializer_class = RolesSerializers
#     permission_classes = [IsAdminRole]

#     def get_object(self):
#         try:
#             pk = self.kwargs.get('pk')
#             return Roles.objects.get(id=pk)
#         except Roles.DoesNotExist:
#             return None

#     def delete(self, request, *args, **kwargs):
#         role = self.get_object()
#         if role is None:
#             return Response('Role Not Exist', status.HTTP_200_OK)
#         if role.name.lower() == 'admin' or role.name.lower() == 'egresado':
#             return Response('No se puede borrar este rol', status.HTTP_200_OK)
#         role.delete()

#         return Response( 'Ok', status.HTTP_200_OK)
