from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializers.eventos.eventos_serialziers import EventosSerializers, EventosSerializersView
from ....models.models import Eventos
from rest_framework import status

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@method_decorator(cache_page(60 * 5), name='dispatch')
class EventosView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = EventosSerializersView(
            Eventos.objects.all().select_related("area", "subArea", "userCreate"), many=True, meta=meta)
        return Response(data.data, status.HTTP_200_OK)


class SaveEventosView(APIView):

    def post(self, request, *args, **kwargs):
        data = EventosSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateEventosView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Eventos.objects.get(pk=pk)
            return seccionId
        except Eventos.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Evento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = EventosSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)

        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


class DeleteEventosView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            eventos = Eventos.objects.get(pk=pk)
            return eventos
        except Eventos.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Evento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)

        return Response("Delete Success", status.HTTP_200_OK)
