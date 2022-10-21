from ..modules import ListAPIView, CreateAPIView, Response, status, UpdateAPIView
from ....models import Document_types
from ...serializers.document.document_serializers import DocumentSerializers


class DocumentListView(ListAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = DocumentSerializers(data, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class DocumentCreateView(CreateAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def post(self, request, *args, **kwargs):
        documentSerializers = DocumentSerializers(data=request.data)
        if documentSerializers.is_valid():
            documentSerializers.save()
            return Response(documentSerializers.data, status=status.HTTP_200_OK)
        return Response(documentSerializers.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentUpdateView(UpdateAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return Document_types.objects.get(pk=pk)
        except Document_types.DoesNotExist:
            raise Response({'message': "Not Found"},
                           status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        document = self.get_object()
        documentSerializers = DocumentSerializers(document, data=request.data)
        if documentSerializers.is_valid():
            documentSerializers.save()
            return Response(documentSerializers.data, status=status.HTTP_200_OK)
        return Response(documentSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
