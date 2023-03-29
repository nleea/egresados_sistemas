from rest_framework.views import APIView
from ...serializers.advertissement.advertisement_serialziers import AdvertisementSerializers,AdvertisementSerializersView
from ....models.models import Anuncio
from rest_framework.response import Response
from .....helpers.create_response import create_response
from rest_framework import status

class AdvertisementView(APIView):
   
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = AdvertisementSerializersView(Anuncio.objects.all(),many=True,meta=meta)
        response, code = create_response(status.HTTP_200_OK,"",data.data)
        return Response(response,code)


class SaveAdvertisementView(APIView):
    
    def post(self, request, *args, **kwargs):
        data = AdvertisementSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user,redes=request.data["redes"])
            response,code=create_response(status.HTTP_200_OK,"Success","Success")
            return Response(response,code)

        response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",data.errors)
        return Response(response,code)


class UpdateCategoryView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Anuncio.objects.get(pk=pk)
            return seccionId
        except Anuncio.DoesNotExist:
            return None


    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Anuncio {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)

        instance = AdvertisementSerializers(instanceOrNone,data=request.data,partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            response, code = create_response(status.HTTP_200_OK,"Success","Success")
            return Response(response,code)

        response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request", instance.errors)
        return Response(response,code)

class DeleteCategoryView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
    
    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            subCategoria = Anuncio.objects.get(pk=pk)
            return subCategoria
        except Anuncio.DoesNotExist:
            return None


    def delete(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Anuncio {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request", "Error")

        response,code = create_response(status.HTTP_200_OK,"Sucess", "Delete Success")
        return Response(response,code)
