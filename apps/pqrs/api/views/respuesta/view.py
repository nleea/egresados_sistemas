from rest_framework.views import APIView
from ...serializers.respuesta.respuesta_serializers import RespuestaSerializers, RespuestaPqrsSerializers
from ....models.models import Respuesta, Pqrs
from rest_framework.response import Response
from rest_framework import status
from ...serializers.pqrs.pqrs_serialziers import PqrsRespuestaSerializers


class RespuestaView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = RespuestaSerializers(
            Respuesta.objects.all(), many=True, meta=meta)
        return Response(data.data, status.HTTP_200_OK,)


class SaveRespuestaView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        data = RespuestaSerializers(data=request.data)

        if data.is_valid():
            data.save(
                anexo=request.data["anexo"], pqrs=request.data["pqrs"], userCreate=request.user)
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

    def delete(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Respuesta {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
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

        instance = RespuestaSerializers(instanceOrNone, data=request.data) # type: ignore
        if instance.is_valid():
            instance.save(anexo=request.data["anexo"], userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)

        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


class RespuestasQuery(APIView):

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            pqrs = Pqrs.objects.filter(pk=pk)
            seccionId = Respuesta.objects.filter(pqrs=pqrs[0].pk)
            return seccionId, pqrs
        except (Pqrs.DoesNotExist, Respuesta.DoesNotExist):
            return None, None

    def get(self, request, *args, **kwargs):

        respuesta, pqrs = self.get_object()
        if respuesta is None or pqrs is None:
            return Response("not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        data = RespuestaPqrsSerializers(respuesta, many=True)
        pqrsRespuesta = PqrsRespuestaSerializers(pqrs, many=True)
        resp = {
            "pqrs": pqrsRespuesta.data[0],
            "respuestas": data.data
        }
        return Response(resp, status.HTTP_200_OK)
