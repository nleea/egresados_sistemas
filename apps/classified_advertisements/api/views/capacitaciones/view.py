from rest_framework.views import APIView
from ...serializers.tipoCapacitacion.capacitacionSerializers import CapacitacionesSerializers
from ....models.models import TiposCapacitaciones
from rest_framework.response import Response
from rest_framework import status
from ..Base.BaseView import ViewPagination


class CapacitacionesView(ViewPagination):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        results = self.paginate_queryset(
            TiposCapacitaciones.objects.all())

        data = CapacitacionesSerializers(
            results, many=True, meta=meta)
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

    def delete(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Capacitacion {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)

        return Response("Delete Success", status.HTTP_200_OK)
