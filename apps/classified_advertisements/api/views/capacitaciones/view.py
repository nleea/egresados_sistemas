from rest_framework.views import APIView
from ...serializers.tipoCapacitacion.capacitacionSerializers import CapacitacionesSerializers,CapacitacionesSerializersView
from ....models.models import TiposCapacitaciones
from rest_framework.response import Response
from rest_framework import status
from ..Base.BaseView import ViewPagination

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator 
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch') 
class CapacitacionesView(ViewPagination):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = CapacitacionesSerializersView(
             self.paginate_queryset(TiposCapacitaciones.objects.select_related("userCreate","userUpdate").filter(visible=True)), many=True, meta=meta)
        paginated_data = self.get_paginated_response(data.data).data

        if paginated_data is None:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
        return Response(paginated_data, status.HTTP_200_OK)


class SaveCapacitacionesView(APIView):

    def post(self, request, *args, **kwargs):
        data = CapacitacionesSerializers(data=request.data)

        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK)

        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateCapacitacionesView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = TiposCapacitaciones.objects.get(pk=pk)
            return seccionId
        except TiposCapacitaciones.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Capacitacion {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = CapacitacionesSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)

        return Response(instance.errors,  status.HTTP_400_BAD_REQUEST)


class DeleteCapacitacionesView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            subCategoria = TiposCapacitaciones.objects.get(pk=pk)
            return subCategoria
        except TiposCapacitaciones.DoesNotExist:
            return None
    
    def bulk_delete(self, ids):
        try:
            resulstForDelete = TiposCapacitaciones.objects.filter(pk__in=ids)
            for _,instance in enumerate(resulstForDelete):
                instance.visible = False 

            TiposCapacitaciones.objects.bulk_update(resulstForDelete,["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Capacitacion {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = CapacitacionesSerializers(
            instanceOrNone, data={"visible":False}, partial=True)
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete", status.HTTP_400_BAD_REQUEST)
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)

        return Response("Delete Success", status.HTTP_200_OK)
