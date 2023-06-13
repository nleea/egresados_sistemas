from rest_framework.views import APIView
from ...serializers.momento.momento_serializers import MomentSerializers
from ....models.models import TipoMomento
from rest_framework.response import Response
from rest_framework import status
from ..BaseView import BaseView

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class MomentView(APIView):

    def get_meta(self):
        if "meta" in self.request.headers:
            return self.request.headers["meta"]
        return None

    def get(self, request, *args, **kwargs):
        data = MomentSerializers(
            TipoMomento.objects.filter(visible=True), many=True, meta=self.get_meta())
        return Response(data.data, status.HTTP_200_OK)


class SaveMomentsView(APIView):

    def post(self, request, *args, **kwargs):
        data = MomentSerializers(data=request.data)

        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK,)
        return Response(data.errors, "Bad Request")


class DeleteMomentsView(BaseView):

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = TipoMomento.objects.get(pk=pk)
            return seccionId
        except TipoMomento.DoesNotExist:
            return None

    def bulk_delete(self, ids):
        try:
            resulstForDelete = TipoMomento.objects.filter(pk__in=ids)
            for _, instance in enumerate(resulstForDelete):
                instance.visible = False

            TipoMomento.objects.bulk_update(resulstForDelete, ["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Momento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = MomentSerializers(
                instanceOrNone, data={"visible": False}, partial=True)
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete", status.HTTP_400_BAD_REQUEST)

            return Response("Delete", status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UpdateMomentsView(BaseView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = TipoMomento.objects.get(pk=pk)
            return seccionId
        except TipoMomento.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Momento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = MomentSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)
