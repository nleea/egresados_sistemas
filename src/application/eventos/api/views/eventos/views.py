from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializers.eventos.eventos_serialziers import (
    EventosSerializers,
    EventosAsistenciaSerializersView,
)
from ....models.models import Eventos
from rest_framework import status
from ....models.models import User
from src.send_email import send_email_list
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
import threading
from django.shortcuts import render

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class EventosTe(APIView):
    def get(self, request, *args, **kwargs):
        evento = Eventos.objects.last()

        if not evento:
            return None

        context = {
            "nombre_actividad": evento.nombre_actividad,
            "objectivo": evento.objectivo,
            "fecha": evento.fecha,
            "hora": evento.hora,
            "lugar": evento.lugar,
        }
        return render(request, "confirm_mensaje.html", context)


class SaveEventosView(APIView):
    def post(self, request, *args, **kwargs):
        data = EventosSerializers(data=request.data)
        if data.is_valid():
            try:
                evento = data.save(userCreate=request.user)
                custom_email = request.data.get("customEmails", [])
                user = User.objects.all().defer("groups")
                evento_data = {
                    "nombre_actividad": evento.nombre_actividad,
                    "objectivo": evento.objectivo,
                    "fecha": evento.fecha,
                    "hora": evento.hora,
                    "lugar": evento.lugar,
                    "id": evento.id,
                }
                threading_emails = threading.Thread(
                    target=send_email_list,
                    args=(user, evento_data, custom_email),
                )
                threading_emails.start()
                return Response("Success", status.HTTP_200_OK)
            except Exception as e:
                return Response(e.args, status.HTTP_400_BAD_REQUEST)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.eventos_interactor import BaseViewSetFactory

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


#@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class EventosViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action in ["get"]:
            return EventosAsistenciaSerializersView
        return EventosSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def post(self, request, *args, **kwargs):
        payload, status = self.controller.post(
            request.data, extra={"userCreate": request.user}
        )
        return Response(data=payload, status=status)

    def put(self, request, *args, **kwargs):
        instance_id = kwargs.get("id", "")
        payload, status = self.controller.put(int(instance_id), request.data)
        return Response(data=payload, status=status)

    def delete(self, request, *args, **kwargs):
        instance_id = kwargs.get("id", "")

        if "ids" in request.data:
            payload, status = self.controller.delete(
                None, request.data.get("ids", None)
            )
            return Response(data=payload, status=status)

        payload, status = self.controller.delete(int(instance_id), request.data)
        return Response(data=payload, status=status)

    def get(self, request, *args, **kwargs):
        status_evento = request.GET.get("status", None)
        order_evento = request.GET.get("order", "-id")
        start_evento = request.GET.get("startdate", None)
        end_evento = request.GET.get("enddate", None)

        rol = request.user.groups.filter(name="Admin").exists()
        

        payload, status = self.controller.get_eventos(
            rol,
            request.user,
            status=status_evento,
            order=order_evento,
            start=start_evento,
            end=end_evento,
        )

        return Response(data=payload, status=status)
