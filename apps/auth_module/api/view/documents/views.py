from ..modules import ListAPIView, CreateAPIView, Response, status, UpdateAPIView, IsAdminRole, DestroyAPIView
from ....models import Document_types
from ...serializers.document.document_serializers import DocumentSerializers


class DocumentListView(ListAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = DocumentSerializers(data, many=True)
        return Response(serializers.data, status.HTTP_200_OK)


class DocumentCreateView(CreateAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def post(self, request, *args, **kwargs):
        documentSerializers = DocumentSerializers(data=request.data)
        if documentSerializers.is_valid():
            documentSerializers.save()
            return Response(documentSerializers.data,  status.HTTP_200_OK)
        return Response(documentSerializers.errors, status.HTTP_400_BAD_REQUEST)


class DocumentUpdateView(UpdateAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def get_object(self):

        try:
            pk = self.kwargs.get('pk')
            return Document_types.objects.get(pk=pk)
        except Document_types.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        document = self.get_object()

        if document is None:
            return Response(documentSerializers.errors, status.HTTP_400_BAD_REQUEST) #type: ignore

        try:
            documentSerializers = DocumentSerializers(
                document, data=request.data)
            if documentSerializers.is_valid():
                documentSerializers.save()
                return Response(documentSerializers.data, status.HTTP_200_OK)
            return Response(documentSerializers.errors, status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class DocumentDestroyView(DestroyAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers
    permission_classes = [IsAdminRole]

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Document_types.objects.get(id=pk)
        except Document_types.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        document = self.get_object()
        if document is None:
            return Response('Type document Not Exist', status.HTTP_200_OK)
        document.delete()

        return Response('Ok', status.HTTP_200_OK)
