from rest_framework.generics import CreateAPIView,ListAPIView
from ...serializers.advertissement.advertisement_serialziers import AdvertisementSerializers,AdvertisementSerializersView
from ....models.models import Anuncio
from rest_framework.response import Response
from .....helpers.create_response import create_response
from rest_framework import status

class AdvertisementView(ListAPIView):
   
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = AdvertisementSerializersView(Anuncio.objects.all(),many=True,meta=meta)
        response, code = create_response(status.HTTP_200_OK,"Sucess",data.data)
        return Response(response,code)


class SaveAdvertisementView(CreateAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AdvertisementSerializers
    
    def post(self, request, *args, **kwargs):
        data = AdvertisementSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user,redes=request.data["redes"])
            response,code=create_response(status.HTTP_200_OK,"Success","Success")
            return Response(response,code)

        response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",data.errors)
        return Response(response,code)