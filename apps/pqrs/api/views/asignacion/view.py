from rest_framework.views import APIView
from ...serializers.asignacion.asignacion_serializers import AsignacionSerializers, AsignacionSerializerView
from ...serializers.pqrs.pqrs_serialziers import PqrsSerializersView

from ....models.models import Asignacion, Pqrs
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .....auth_module.models import User
from .....auth_module.api.serializers.user.users_serializers import UserSerializersSimple

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AsignacionView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        user = User.objects.only("email", "id", "username").get(pk=1)
        queryset = Asignacion.objects.defer("userCreate", "userUpdate", "pqrs__userCreate_id",
                                            "pqrs__userUpdate", "pqrs__tipopqrs__userCreate_id",
                                            "pqrs__tipopqrs__userUpdate_id").select_related(
            "pqrs", "pqrs__tipopqrs","pqrs__persona").filter(funcionarioId=user.id,visible=True)
        data = AsignacionSerializerView(queryset, many=True)
        return Response({"pqrs": [x["pqrs"] for x in data.data]}, status.HTTP_200_OK)


class AsignacionPqrsView(APIView):
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        roles = request.user.roles.get(name="Admin")

        if roles:
            pqrs_filter = Pqrs.objects.select_related(
                "persona", "tipopqrs").filter(status="AC")
            data = PqrsSerializersView(pqrs_filter, many=True, meta=True)
            return Response(data.data, status.HTTP_200_OK)


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
    
    def bulk_delete(self, ids):
        try:
            resulstForDelete = Asignacion.objects.filter(pk__in=ids)
            for _,instance in enumerate(resulstForDelete):
                instance.visible = False 

            Asignacion.objects.bulk_update(resulstForDelete,["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])
        
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Asignacion {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST,)
        try:
            instance = AsignacionSerializers(instanceOrNone, data={"visible": False},partial=True)

            if instance.is_valid():
                instance.save(userUpdate=request.user)
                return Response("Success", status.HTTP_200_OK)

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
