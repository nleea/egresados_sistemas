from rest_framework.views import APIView
from ...serializers.asignacion.asignacion_serializers import AsignacionSerializers, AsignacionSerializerView
from ....models.models import Asignacion
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .....auth_module.models import User
from .....auth_module.api.serializers.user.users_serializers import UserSerializersSimple

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AsignacionView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        user = User.objects.only("email","id","username").get(pk=1)
        queryset = Asignacion.objects.defer("pqrs__persona_id","userCreate","userUpdate","pqrs__userCreate_id","pqrs__userUpdate","pqrs__tipopqrs__userCreate_id","pqrs__tipopqrs__userUpdate_id").select_related(
            "pqrs","pqrs__tipopqrs").filter(funcionarioId=user.id)
        data = AsignacionSerializerView(queryset, many=True)
        serialziersUser = UserSerializersSimple([user], many=True)
        return Response({**serialziersUser.data[0], "pqrs": [x["pqrs"] for x in data.data]}, status.HTTP_200_OK)


class SaveAsignacionView(APIView):

    def post(self, request, *args, **kwargs):
        data = AsignacionSerializers(data=request.data)

        if data.is_valid():
            data.save(funcionarioId=request.user.id,
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
