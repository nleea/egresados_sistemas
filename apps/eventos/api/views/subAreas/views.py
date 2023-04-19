from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializers.eventos.eventos_sub_area_serializers import EventosSubAreaSerializers, EventosSubAreaSerializersView
from ....models.models import SubAreaEventos
from rest_framework import status


class EventosSubAreaView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = EventosSubAreaSerializersView(
            SubAreaEventos.objects.all(), many=True, meta=meta)

        return Response(data.data, status.HTTP_200_OK)


class EventosQuery(APIView):

    def post(self, request, *args, **kwargs):
        if 'area' in request.data:
            subAreas = SubAreaEventos.objects.filter(area=request.data["area"])
            data = EventosSubAreaSerializersView(subAreas, many=True)
            return Response(data.data, status.HTTP_200_OK)
        else:
            return Response(f"Filter object {request.data} not found",   status.HTTP_200_OK)


class SaveEventosSubAreaView(APIView):

    def post(self, request, *args, **kwargs):
        data = EventosSubAreaSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateEventosSubAreaView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = SubAreaEventos.objects.get(pk=pk)
            return seccionId
        except SubAreaEventos.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Evento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = EventosSubAreaSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


class DeleteEventosSubAreaView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            eventos = SubAreaEventos.objects.get(pk=pk)
            return eventos
        except SubAreaEventos.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Evento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
        return Response("Delete Success", status.HTTP_200_OK)
