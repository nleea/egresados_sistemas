from rest_framework.views import APIView
from ...serializers.advertissement.advertisement_serialziers import AdvertisementSerializers, AdvertisementSerializersView
from ...serializers.subCategory.subCategory_serializers import SubCategorySerializersView
from ....models.models import Anuncio, SubCategoria
from rest_framework.response import Response
from rest_framework import status
from ..Base.BaseView import ViewPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator 

class AdvertisementsQueryView(APIView):

    def post(self, request, *args, **kwargs):
        results = []
        if ("categoryId" in request.data):
            results = SubCategorySerializersView(SubCategoria.objects.filter_subcategory_has_category(
                request.data["categoryId"]), many=True).data
        elif ("subCategoryId" in request.data):
            anuncio = Anuncio.objects.filter_Advertisement_subCategory(
                request.data["subCategoryId"])
            results = AdvertisementSerializersView(anuncio, many=True).data

        return Response(results, status.HTTP_200_OK,)

@method_decorator(cache_page(60 * 5), name='dispatch') 
class AdvertisementView(ViewPagination):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        anuncios = Anuncio.objects.select_related("subCategoria","userCreate","userUpdate").prefetch_related("redes","tipo_capacitacion").all()
        
        results = self.paginate_queryset(anuncios)
        data = AdvertisementSerializersView(
            results, many=True, meta=meta)
        paginated_data = self.get_paginated_response(data.data).data
        if paginated_data is None:
            return Response("error", status.HTTP_400_BAD_REQUEST)
        return Response(paginated_data, status.HTTP_200_OK)


class SaveAdvertisementView(APIView):

    def post(self, request, *args, **kwargs):
        data = AdvertisementSerializers(data=request.data)
        redes = []
        if data.is_valid():
            if 'redes' in request.data:
                redes = request.data["redes"]
            data.save(userCreate=request.user, redes=redes)
            return Response("Success", status.HTTP_200_OK)

        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


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
            return Response("Anuncio {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = AdvertisementSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success",  status.HTTP_200_OK)

        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


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
            return Response("Anuncio {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
        return Response("Delete Success", status.HTTP_200_OK)
