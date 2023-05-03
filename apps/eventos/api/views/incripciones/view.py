from rest_framework.views import APIView
from rest_framework.response import Response
from ....models.models import Inscripcion, User
from ...serializers.eventos.inscripciones import InscripcionesSerializersView, InscripcionesSerializers
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from apps.send_email import send_notification_mail


@method_decorator(cache_page(60 * 5), name='dispatch')
class InscripcionView(APIView):
    def get(self, request, *args, **kwargs):

        param = request.GET.get("evento", None)

        if param:
            results = Inscripcion.objects.defer("user__roles", "evento__userCreate_id", "evento__userUpdate_id", "evento__tipo__userCreate_id",
                                                "evento__tipo__userUpdate_id", "evento__subArea__userUpdate_id",
                                                "evento__subArea__userCreate_id", "evento__area__userCreate_id",
                                                "evento__area__userUpdate_id").select_related("evento", "evento__tipo",
                                                                                              "evento__subArea",
                                                                                              "evento__area").prefetch_related("user").filter(evento=param)
            inscripcionesResulst = InscripcionesSerializersView(
                results, many=True)
            return Response(inscripcionesResulst.data, 200)
        return Response("Evento Not found", 404)


class IncripcionSave(APIView):

    def post(self, request, *args, **kwargs):
        if 'evento' in request.data:
            user = User.objects.all().defer("roles")
            inscripcionesResulst = InscripcionesSerializers(data=request.data)
            if inscripcionesResulst.is_valid():
                try:
                    send_notification_mail.delay(
                        [x.email for x in user],"Test")  # type: ignore
                    inscripcionesResulst.save(user=user)
                    return Response("Inscripciones creadas", 200)
                except Exception as e:
                    return Response(e, 400)
            return Response(inscripcionesResulst.errors, 404)
        return Response("Evento Not found", 404)


class GenerateQrCode(APIView):
    pass
