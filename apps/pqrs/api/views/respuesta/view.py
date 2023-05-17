from rest_framework.views import APIView
from ...serializers.respuesta.respuesta_serializers import RespuestaSerializers, RespuestaSerializersView
from ...serializers.pqrs.pqrs_serialziers import PqrsSerializers
from ....models.models import Respuesta, Pqrs
from rest_framework.response import Response
from rest_framework import status
from ...serializers.pqrs.pqrs_serialziers import PqrsSerializersView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models import Prefetch

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class RespuestaView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = RespuestaSerializersView(
            Respuesta.objects.select_related("pqrs").filter(visible=True), many=True, meta=meta)
        return Response(data.data, status.HTTP_200_OK,)


class SaveRespuestaView(APIView):

    def post(self, request, *args, **kwargs):
        data = RespuestaSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            if "status" in request.data:
                pqrsResulst = Pqrs.objects.get(pk=request.data["pqrs"])
                resulst = PqrsSerializers(
                    pqrsResulst, {"status": request.data["status"]}, partial=True)
                if resulst.is_valid():
                    resulst.save()
            return Response("Sucess", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class DeleteRespuestaView(APIView):

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Respuesta.objects.get(pk=pk)
            return seccionId
        except Respuesta.DoesNotExist:
            return None
    
    def bulk_delete(self, ids):
        try:
            resulstForDelete = Respuesta.objects.filter(pk__in=ids)
            for _,instance in enumerate(resulstForDelete):
                instance.visible = False 

            Respuesta.objects.bulk_update(resulstForDelete,["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])
        
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Respuesta {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = RespuestaSerializers(
                instanceOrNone, data={"visible": False}, partial=True)  # type: ignore
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Success", status.HTTP_200_OK)
            return Response("Delete", status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UpdateRespuestaView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Respuesta.objects.get(pk=pk)
            return seccionId
        except Respuesta.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Respuesta {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = RespuestaSerializers(
            instanceOrNone, data=request.data)  # type: ignore
        if instance.is_valid():
            instance.save(anexo=request.data["anexo"], userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)

        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


@method_decorator(cache_page(60 * 5), name='dispatch')
class RespuestasQuery(APIView):

    def query(self, pk):
        try:
            pqrs = Pqrs.objects.defer("userCreate", "userUpdate", "tipopqrs__userCreate", "tipopqrs__userUpdate").prefetch_related(
                Prefetch("respuesta_pqrs", queryset=Respuesta.objects.defer("userCreate", "userUpdate").all())).select_related("tipopqrs", "persona").get(pk=pk)
            # type:ignore
            respuestas = pqrs._prefetched_objects_cache["respuesta_pqrs"]#type:ignore
            return pqrs, respuestas
        except (Pqrs.DoesNotExist):
            return None, None

    def post(self, request, *args, **kwargs):

        pqrsId = request.data["pqrs"]
        pqrs, respuesta = self.query(pqrsId)

        if pqrs is None:
            return Response("PQRS with id {} not exist".format(pqrsId), status.HTTP_400_BAD_REQUEST)

        resulst = PqrsSerializersView([pqrs], many=True)
        resulst_respuestas = RespuestaSerializersView(
            respuesta, many=True, extra=False)

        response = {
            "pqrs": resulst.data,
            "respuestas": resulst_respuestas.data
        }

        return Response(response, status.HTTP_200_OK)
