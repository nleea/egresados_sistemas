from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializers.eventos.eventos_serialziers import EventosSerializers, EventosSerializersView
from ...serializers.eventos.inscripciones import InscripcionesSerializers
from ....models.models import Eventos
from rest_framework import status
from ....models.models import User
from apps.send_email import send_email_list
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
import threading

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class EventosView(APIView):

    def get(self, request, *args, **kwargs):
        mine = request.GET.get("mine", None)
        data = None
        if mine:
            data = EventosSerializersView(
                Eventos.objects.defer("tipo__userCreate_id","tipo__userUpdate_id","subArea__userCreate_id","subArea__userUpdate_id").select_related("area", "subArea", "userCreate", "userUpdate", "tipo").filter(visible=True, userCreate__id=request.user.id), many=True, meta=True).order_by("-id")
        else:
            data = EventosSerializersView(
                Eventos.objects.defer("tipo__userCreate_id","tipo__userUpdate_id","subArea__userCreate_id","subArea__userUpdate_id").select_related("area",
                                               "subArea", "userCreate", 
                                               "userUpdate", "tipo").filter(visible=True).order_by("-id"), many=True, meta=True)

        return Response(data.data, status.HTTP_200_OK)


class SaveEventosView(APIView):

    def post(self, request, *args, **kwargs):

        data = EventosSerializers(data=request.data)
        if data.is_valid():
            evento = data.save(userCreate=request.user)
            user = User.objects.all().defer("groups")
            inscripcionesResulst = InscripcionesSerializers(
                data={"evento": evento.pk})
            if inscripcionesResulst.is_valid():
                try:
                    evento = inscripcionesResulst.validated_data["evento"] # type: ignore
                    threading_emails = threading.Thread(
                        target=send_email_list, args=(user, evento))
                    threading_emails.start()
                    inscripcionesResulst.save(user=user)
                except Exception as e:
                    return Response(e, status.HTTP_400_BAD_REQUEST)
            return Response("Success", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateEventosView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")  # type: ignore
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

    def bulk_delete(self, ids):
        try:
            resulstForDelete = Eventos.objects.filter(pk__in=ids)
            for _, instance in enumerate(resulstForDelete):
                instance.visible = False

            Eventos.objects.bulk_update(resulstForDelete, ["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Evento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = EventosSerializers(
                instanceOrNone, data={"visible": False}, partial=True)
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete", status.HTTP_400_BAD_REQUEST)
            return Response("Success", status.HTTP_200_OK)
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
