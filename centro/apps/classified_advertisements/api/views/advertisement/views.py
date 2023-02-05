from rest_framework.views import APIView
from ...serializers.advertissement.advertisement_serialziers import AdvertisementSerializers
from ....models.models import Anuncio
from rest_framework.response import Response
from .....helpers.create_response import create_response
from rest_framework import status

class AdvertisementView(APIView):
   
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = AdvertisementSerializers(Anuncio.objects.all(),many=True,meta=meta)
        return Response(data.data)


class SaveAdvertisementView(APIView):

    def post(self, request, *args, **kwargs):
        data = AdvertisementSerializers(data=request.data)
        if data.is_valid():
            data.save(persona_id=request.user,subCategori=request.data["subCategori"])
            response,code=create_response(status.HTTP_200_OK,"Success","Success")
            return Response(response,code)

        response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",data.errors)
        return Response(response,code)
