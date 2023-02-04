from rest_framework.views import APIView
from ...serializers.advertissement.advertisement_serialziers import AdvertisementSerializers
from ....models.models import Anuncio
from rest_framework.response import Response

class AdvertisementView(APIView):
   
    
    def get(self, request, *args, **kwargs):
        data = AdvertisementSerializers(Anuncio.objects.all(),many=True)
        return Response(data.data)