from ..modules import ListAPIView, Response, UpdateAPIView, status,  DestroyAPIView, IsAdminRole
from ....models import Resources
from ...serializers.resources.resources_serializers import ResourcesSerializers


class ResourcesListView(ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = ResourcesSerializers(data, many=True)
        return Response(serializers.data, status.HTTP_200_OK)


class ResourcesUpdateView(UpdateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            return {'response': 'Not Found', 'code': status.HTTP_400_BAD_REQUEST}

    def path(self, request, *args, **kwargs):
        resources = self.get_object()
        if type(resources) is dict:
            return Response(resources['response'], resources['code'])
        resourcesSerializers = ResourcesSerializers(
            resources, data=request.data)
        if resourcesSerializers.is_valid():
            resourcesSerializers.save()
            return Response(resourcesSerializers.data, status.HTTP_200_OK)
        return Response(resourcesSerializers.errors, status.HTTP_400_BAD_REQUEST)


class ResourcesDestroyView(DestroyAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializers
    permission_classes = [IsAdminRole]

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Resources.objects.get(id=pk)
        except Resources.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        resources = self.get_object()
        if resources is None:
            return Response('Resources Not Exist', status.HTTP_200_OK)
        resources.delete()

        return Response('Ok', status.HTTP_200_OK)
