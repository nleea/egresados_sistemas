from rest_framework.views import APIView
from ...serializers.anexo.anexo_serializers import AnexoSerializers
from ....models.models import Anexo
from rest_framework.response import Response
from rest_framework import status


class AnexoView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = AnexoSerializers(Anexo.objects.all(), many=True, meta=meta)
        return Response(data.data, status.HTTP_200_OK)


class SaveAnexoView(APIView):

    def post(self, request, *args, **kwargs):
        data = AnexoSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class DeleteAnexoView(APIView):

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Anexo.objects.get(pk=pk)
            return seccionId
        except Anexo.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Anexo {} not exist".format(self.kwargs.get('pk')),  status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
            return Response("Delete", status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UpdateAnexoView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Anexo.objects.get(pk=pk)
            return seccionId
        except Anexo.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Anexo {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = AnexoSerializers(instanceOrNone, data=request.data)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)

        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)
