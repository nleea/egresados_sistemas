from rest_framework.views import APIView
from ...serializers.pqrs.pqrs_serialziers import PqrsSerializers, PqrsSerializersView
from ....models.models import Pqrs,Asignacion
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db import models

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class PqrsView(APIView):

    def get_pqrs_date(self,status,order,start,end):
        pqrs_filter = Pqrs.objects.defer("tipopqrs__userCreate_id","tipopqrs__userUpdate_id","userUpdate").select_related(
                "persona", "tipopqrs", "userCreate").prefetch_related(
                    models.Prefetch("asignacion_set",queryset=Asignacion.objects.all().defer(
                        "userCreate","userUpdate","funcionarioId","fecha_asignacion","updateAt","createdAt"))).filter(userCreate=self.request.user.id,status=status, createdAt__range=[start,end],  visible=True).order_by(order)
        data = PqrsSerializersView(pqrs_filter, many=True, meta=False)
        
        return data


    def get(self, request, *args, **kwargs):
        roles = request.user.groups.get(name="Admin")

        status_pqrs = request.GET.get("status","AC")
        order_pqrs = request.GET.get("order","-id")
        start_pqrs = request.GET.get("startdate",None)
        end_pqrs = request.GET.get("enddate",None)

        if start_pqrs and end_pqrs:
            results = self.get_pqrs_date(status_pqrs,order_pqrs,start_pqrs,end_pqrs)
            return Response(results.data,status.HTTP_200_OK)

        if roles:
            pqrs_filter = Pqrs.objects.defer("tipopqrs__userCreate_id","tipopqrs__userUpdate_id","userCreate", "userUpdate").select_related(
                "persona", "tipopqrs").prefetch_related(models.Prefetch("asignacion_set",queryset=Asignacion.objects.all().defer("userCreate","userUpdate","funcionarioId","fecha_asignacion","updateAt","createdAt"))).filter(visible=True,status=status_pqrs).order_by(order_pqrs)
            data = PqrsSerializersView(pqrs_filter, many=True, meta=False)
            return Response(data.data, status.HTTP_200_OK)
        else:
            pqrs_filter = Pqrs.objects.defer("tipopqrs__userCreate_id","tipopqrs__userUpdate_id","userUpdate").select_related(
                "persona", "tipopqrs", "userCreate").prefetch_related(models.Prefetch("asignacion_set",queryset=Asignacion.objects.all().defer("userCreate","userUpdate","funcionarioId","fecha_asignacion","updateAt","createdAt"))).filter(userCreate=request.user.id,visible=True).order_by(order_pqrs)
            data = PqrsSerializersView(pqrs_filter, many=True, meta=False)
            return Response(data.data, status.HTTP_200_OK)


class SavePqrsView(APIView):

    def post(self, request, *args, **kwargs):
        data = PqrsSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class DeletePqrsView(APIView):

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Pqrs.objects.get(pk=pk)
            return seccionId
        except Pqrs.DoesNotExist:
            return None

    def bulk_delete(self, ids):
        try:
            resulstForDelete = Pqrs.objects.filter(pk__in=ids)
            for _, instance in enumerate(resulstForDelete):
                instance.visible = False

            Pqrs.objects.bulk_update(resulstForDelete, ["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Pqrs {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = PqrsSerializers(
                instanceOrNone, data={"visible": False}, partial=True)
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete", status.HTTP_200_OK)
            return Response("Delete", status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UpdatePqrsView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Pqrs.objects.get(pk=pk)
            return seccionId
        except Pqrs.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Pqrs {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = PqrsSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)
