from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializers.eventos.eventos_serialziers import (
    EventosSerializers,
    EventosAsistenciaSerializersView,
)
from ...serializers.eventos.inscripciones import InscripcionesSerializers
from ....models.models import Eventos, Asistencia
from rest_framework import status
from ....models.models import User
from django.db import models
from apps.send_email import send_email_list
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
import threading
from django.utils import timezone
from configs.helpers.hour import readeable_hour

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class EventosView(APIView):
    def get_eventos_date(self, order, start_date, end_date):
        results = (
            Eventos.objects.defer(
                "userCreate",
                "userUpdate",
                "area__userCreate",
                "area__userUpdate",
                "subArea__userCreate",
                "subArea__userUpdate",
                "tipo__userCreate",
                "tipo__userUpdate",
            )
            .select_related("area", "subArea", "tipo")
            .filter(
                inscripcion__user=self.request.user.id,  # type:ignore
                fecha__range=[start_date, end_date],
                visible=True,
            )
            .order_by(order)
        )

        return results

    def get(self, request, *args, **kwargs):
        mine = request.GET.get("mine", None)
        status_evento = request.GET.get("status", None)
        order_evento = request.GET.get("order", "-id")
        start_evento = request.GET.get("startdate", None)
        end_evento = request.GET.get("enddate", None)

        rol = request.user.groups.filter(name="admin").exists()

        if rol:
            results = (
                Eventos.objects.defer(
                    "userCreate",
                    "userUpdate",
                    "area__userCreate",
                    "area__userUpdate",
                    "subArea__userCreate",
                    "subArea__userUpdate",
                    "tipo__userCreate",
                    "tipo__userUpdate",
                )
                .filter(visible=True)
                .select_related("area", "subArea", "tipo")
                .order_by(order_evento)
            )
        else:
            if start_evento and end_evento:
                results = self.get_eventos_date(
                    start_date=start_evento, end_date=end_evento, order=order_evento
                )
            else:
                results = (
                    Eventos.objects.defer(
                        "userCreate",
                        "userUpdate",
                        "area__userCreate",
                        "area__userUpdate",
                        "subArea__userCreate",
                        "subArea__userUpdate",
                        "tipo__userCreate",
                        "tipo__userUpdate",
                    )
                    .filter(inscripcion__user=request.user.id, visible=True)
                    .select_related("area", "subArea", "tipo")
                    .order_by(order_evento)
                )

        eventos_asistencia = results.annotate(
            confirm_asistencia=models.Exists(
                Asistencia.objects.filter(
                    evento=models.OuterRef("pk"), user=request.user.id, confirm=True
                )
            ),
            fecha_pasada=models.Case(
                models.When(fecha__lt=timezone.now().date(), then=True),
                default=False,
                output_field=models.BooleanField(),
            ),
        )

        if status_evento:
            eventos_asistencia = eventos_asistencia.filter(fecha_pasada=status_evento)

        resulstSerializers = EventosAsistenciaSerializersView(results, many=True)

        return Response(resulstSerializers.data, status.HTTP_200_OK)


class SaveEventosView(APIView):
    def post(self, request, *args, **kwargs):
        data = EventosSerializers(data=request.data)
        if data.is_valid():
            evento = data.save(userCreate=request.user)
            custom_email = request.data.get("customEmails", [])
            user = User.objects.all().defer("groups")
            try:
                threading_emails = threading.Thread(
                    target=send_email_list,
                    args=(user, evento.id, custom_email),
                )
                threading_emails.start()
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
            return Response(
                "Evento {} not exist".format(self.kwargs.get("pk")),
                status.HTTP_400_BAD_REQUEST,
            )

        instance = EventosSerializers(instanceOrNone, data=request.data, partial=True)
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
            return Response(
                "Evento {} not exist".format(self.kwargs.get("pk")),
                status.HTTP_400_BAD_REQUEST,
            )

        try:
            instance = EventosSerializers(
                instanceOrNone, data={"visible": False}, partial=True
            )
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete", status.HTTP_400_BAD_REQUEST)
            return Response("Success", status.HTTP_200_OK)
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
