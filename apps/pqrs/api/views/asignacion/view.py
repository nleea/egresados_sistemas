from rest_framework.views import APIView
from ...serializers.asignacion.asignacion_serializers import AsignacionSerializers
from ....models.models import Asignacion
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator 

@method_decorator(cache_page(60 * 5), name='dispatch') 
class AsignacionView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = AsignacionSerializers(
            Asignacion.objects.all(), many=True, meta=meta)
        return Response(data.data, status.HTTP_200_OK)


class SaveAsignacionView(APIView):

    def post(self, request, *args, **kwargs):
        data = AsignacionSerializers(data=request.data)

        if data.is_valid():
            data.save(funcionarioId=request.data["funcionarioId"],
                      pqrs=request.data["pqrs"], userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK)

        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class DeleteAsignacionView(APIView):

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Asignacion.objects.get(pk=pk)
            return seccionId
        except Asignacion.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Asignacion {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST,)
        try:
            instanceOrNone.delete()
            return Response("Delete", status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UpdateAsignacionView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Asignacion.objects.get(pk=pk)
            return seccionId
        except Asignacion.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Asignacion {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST,)

        instance = AsignacionSerializers(instanceOrNone, data=request.data)
        if instance.is_valid():

            try:
                instance.save(
                    funcionarioId=request.data["funcionarioId"], userUpdate=request.user)
                return Response("Success", status.HTTP_200_OK)
            except BaseException as e:
                return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)
