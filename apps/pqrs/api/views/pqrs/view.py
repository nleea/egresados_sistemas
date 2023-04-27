from rest_framework.views import APIView
from ...serializers.pqrs.pqrs_serialziers import PqrsSerializers,PqrsSerializersView
from ....models.models import Pqrs
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator 

@method_decorator(cache_page(60 * 5), name='dispatch') 
class PqrsView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = PqrsSerializersView(Pqrs.objects.select_related("persona","tipopqrs").all(), many=True, meta=meta)
        return Response(data.data,status.HTTP_200_OK)


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

    def delete(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Pqrs {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
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

        instance = PqrsSerializers(instanceOrNone, data=request.data,partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)
