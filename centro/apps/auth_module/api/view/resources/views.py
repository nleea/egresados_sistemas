from ..modules import ListAPIView, Response, UpdateAPIView, status, create_response
from ....models import Resources
from ...serializers.resources.resources_serializers import ResourcesSerializers


class ResourcesListView(ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = ResourcesSerializers(data, many=True)
        response, code = create_response(status.HTTP_200_OK, serializers.data)
        return Response(response, status=code)


class ResourcesUpdateView(UpdateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            raise Response(create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found'))

    def path(self, request, *args, **kwargs):
        resources = self.get_object()
        resourcesSerializers = ResourcesSerializers(
            resources, data=request.data)
        if resourcesSerializers.is_valid():
            resourcesSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, resourcesSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, resourcesSerializers.errors)
        return Response(response, status=code)
