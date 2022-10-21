from ..modules import CreateAPIView, ListAPIView, Response, UpdateAPIView, status, create_response
from ....models import Resources
from ...serializers.resources.resources_serializers import ResourcesSerializers


class ResourcesListView(ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = ResourcesSerializers(data, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ResourcesCreateView(CreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializers

    def post(self, request, *args, **kwargs):
        resourcesSerializers = ResourcesSerializers(data=request.data)
        if resourcesSerializers.is_valid():
            resourcesSerializers.save()
            return Response(resourcesSerializers.data, status=status.HTTP_200_OK)
        return Response(resourcesSerializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourcesUpdateView(UpdateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            raise Response(create_response(
                "", status.HTTP_400_BAD_REQUEST, {'message': 'Not Found'}))

    def put(self, request, *args, **kwargs):
        resources = self.get_object()
        resourcesSerializers = ResourcesSerializers(
            resources, data=request.data)
        if resourcesSerializers.is_valid():
            resourcesSerializers.save()
            return Response(resourcesSerializers.data, status=status.HTTP_200_OK)
        return Response(resourcesSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
