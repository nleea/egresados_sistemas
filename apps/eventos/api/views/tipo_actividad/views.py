from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializers.eventos.eventos_tipo import TipoEventosSerializers
from ....models.models import TipoEvento
from rest_framework import status

class TipoEventosView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = TipoEventosSerializers(
            TipoEvento.objects.select_related("userCreate","userUpdate").filter(visible=True), many=True, meta=meta)

        return Response(data.data, status.HTTP_200_OK)


class SaveTipoEventos(APIView):

    def post(self, request, *args, **kwargs):
        data = TipoEventosSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateTipoEventosView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = TipoEvento.objects.get(pk=pk)
            return seccionId
        except TipoEvento.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Evento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = TipoEventosSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


class DeleteTipoEventosView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            eventos = TipoEvento.objects.get(pk=pk)
            return eventos
        except TipoEvento.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Evento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = TipoEventosSerializers(
            instanceOrNone, data={"visible":False}, partial=True)
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete", status.HTTP_400_BAD_REQUEST)

        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
        return Response("Delete Success", status.HTTP_200_OK)
