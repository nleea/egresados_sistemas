from rest_framework.views import APIView
from ...serializers.momento.momento_serializers import MomentSerializers
from ....models.models import TipoMomento
from rest_framework.response import Response
from rest_framework import status
from ..BaseView import BaseView

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator 

@method_decorator(cache_page(60 * 5), name='dispatch') 
class MomentView(APIView):
    
    def get_meta(self) -> object | None:
        if "meta" in self.request.headers:
            return self.request.headers["meta"]
        return None

    def get(self, request, *args, **kwargs):
        data = MomentSerializers(
            TipoMomento.objects.all(), many=True, meta=self.get_meta())
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

    def delete(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Momento {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
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
