from rest_framework.generics import CreateAPIView
from ...serializers.resources.resources_serializers import ResourcesRolesSerializers
from rest_framework import status
from ....models import Resources
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
