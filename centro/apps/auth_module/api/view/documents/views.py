from ..modules import ListAPIView, CreateAPIView, Response, status, UpdateAPIView, create_response
from ....models import Document_types
from ...serializers.document.document_serializers import DocumentSerializers


class DocumentListView(ListAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = DocumentSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'Document', serializers.data)
        return Response(response, status=code)


class DocumentCreateView(CreateAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def post(self, request, *args, **kwargs):
        documentSerializers = DocumentSerializers(data=request.data)
        if documentSerializers.is_valid():
            documentSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Document', documentSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', documentSerializers.errors)
        return Response(response, status=code)


class DocumentUpdateView(UpdateAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return Document_types.objects.get(pk=pk)
        except Document_types.DoesNotExist:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', 'Document Not found')
            return {'response': response, 'code': code}

    def put(self, request, *args, **kwargs):
        document = self.get_object()

        if type(document) is dict:
            return Response(document['response'], document['code'])

        documentSerializers = DocumentSerializers(document, data=request.data)
        if documentSerializers.is_valid():
            documentSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Document Update', documentSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', documentSerializers.errors)
        return Response(response, status=code)
