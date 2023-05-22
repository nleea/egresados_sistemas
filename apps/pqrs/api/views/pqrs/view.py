from rest_framework.views import APIView
from ...serializers.pqrs.pqrs_serialziers import PqrsSerializers, PqrsSerializersView
from ....models.models import Pqrs
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class PqrsView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        roles = request.user.roles.filter(name="Admin")

        if roles:
            pqrs_filter = Pqrs.objects.select_related(
                "persona", "tipopqrs").filter(visible=True)
            data = PqrsSerializersView(pqrs_filter, many=True, meta=True)
            return Response(data.data, status.HTTP_200_OK)
        else:
            pqrs_filter = Pqrs.objects.select_related(
                "persona", "tipopqrs").filter(userCreate=request.user.id,visible=True)
            data = PqrsSerializersView(pqrs_filter, many=True, meta=True)
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
            for _,instance in enumerate(resulstForDelete):
                instance.visible = False 

            Pqrs.objects.bulk_update(resulstForDelete,["visible"])

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
