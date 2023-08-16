from rest_framework.views import APIView
from django.db import models
from rest_framework.response import Response
from ....models.models import Inscripcion, User, Asistencia, Eventos
from ...serializers.eventos.inscripciones import (
    InscripcionesSerializersView,
    InscripcionesSerializers,
    AsistenciaSerializer,
)
from ...serializers.eventos.eventos_serialziers import EventosAsistenciaSerializersView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from apps.send_email import send_notification_mail
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils import timezone

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class InscripcionView(APIView):
    def get(self, request, *args, **kwargs):
        param = request.GET.get("evento", None)

        if param:
            results = (
                Inscripcion.objects.defer(
                    "evento__userCreate_id",
                    "evento__userUpdate_id",
                    "evento__tipo__userCreate_id",
                    "evento__tipo__userUpdate_id",
                    "evento__subArea__userUpdate_id",
                    "evento__subArea__userCreate_id",
                    "evento__area__userCreate_id",
                    "evento__area__userUpdate_id",
                )
                .select_related(
                    "evento", "evento__tipo", "evento__subArea", "evento__area"
                )
                .prefetch_related("user")
                .filter(evento=param)
                .order_by("-id")
            )
            inscripcionesResulst = InscripcionesSerializersView(results, many=True)
            return Response(inscripcionesResulst.data, 200)
        return Response("Evento Not found", 404)


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class InscripcionEventosView(APIView):
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
                inscripcion__user=self.request.user.pk,
                fecha__range=[start_date, end_date],
                visible=True,
            )
            .order_by(order)
        )

        return results

    def get(self, request, *args, **kwargs):
        status_evento = request.GET.get("status", None)
        order_evento = request.GET.get("order", "-id")
        start_evento = request.GET.get("startdate", None)
        end_evento = request.GET.get("enddate", None)

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
            asistire=models.Exists(
                Asistencia.objects.filter(
                    evento=models.OuterRef("pk"), user=request.user.id
                )
            ),
        )

        if status_evento:
            eventos_asistencia = eventos_asistencia.filter(fecha_pasada=status_evento)

        resulstSerializers = EventosAsistenciaSerializersView(
            eventos_asistencia, many=True
        )

        return Response(resulstSerializers.data, 200)


class IncripcionSaveView(APIView):
    def post(self, request, *args, **kwargs):
        evento = request.data.get("evento", None)
        user = request.user

        resulst = InscripcionesSerializers(data={"user": user.pk, "evento": evento})

        if resulst.is_valid():
            inscripcion = resulst.save()
            send_notification_mail.delay([inscripcion.user.email], user.pk, evento)  # type: ignore
            return Response({"message": "Ok"}, status=200)

        return Response(resulst.errors, status=400)


class AsistenciaView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.GET.get("user", None)
        evento = request.GET.get("evento", None)
        user_session = request.user

        resulst = AsistenciaSerializer(
            data={"user": user, "evento": evento}, partial=True
        )

        if resulst.is_valid():
            resulst.save(user_session=user_session, asistencia=True)
            return Response({"message": "Ok"}, status=200)

        return Response(resulst.error_messages, status=400)
