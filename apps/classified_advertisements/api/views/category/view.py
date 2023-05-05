from rest_framework.views import APIView
from ...serializers.category.category_serializers import CategorySerializers,CategorySerializersView
from ....models.models import Categoria
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator 
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')  
class CategoryView(APIView):
   
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = CategorySerializersView(Categoria.objects.select_related("userCreate","userUpdate").all(),many=True,meta=meta)
        return Response(data.data,status.HTTP_200_OK)


class SaveCategoryView(APIView):

    def post(self, request, *args, **kwargs):
        data = CategorySerializers(data=request.data)

        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Sucess",status.HTTP_200_OK)
        return Response(data.errors,status.HTTP_400_BAD_REQUEST)


class UpdateCategoryView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Categoria.objects.get(pk=pk)
            return seccionId
        except Categoria.DoesNotExist:
            return None


    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request","Categoria {} not exist".format(self.kwargs.get('pk')),status.HTTP_400_BAD_REQUEST)

        instance = CategorySerializers(instanceOrNone,data=request.data)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success",status.HTTP_200_OK)
        return Response(instance.errors,status.HTTP_400_BAD_REQUEST)

class DeleteCategoryView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
    
    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            subCategoria = Categoria.objects.get(pk=pk)
            return subCategoria
        except Categoria.DoesNotExist:
            return None


    def delete(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Categoria {} not exist".format(self.kwargs.get('pk')),status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            return Response("Error",status.HTTP_400_BAD_REQUEST)
        
        return Response("Delete Success",status.HTTP_200_OK)
