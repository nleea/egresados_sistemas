from rest_framework.views import APIView
from ...serializers.advertissement.advertisement_serialziers import AdvertisementSerializers, AdvertisementSerializersView, AdvertisementVotoSerializers
from ...serializers.subCategory.subCategory_serializers import SubCategorySerializersView
from ....models.models import Anuncio, SubCategoria, VotoAnuncio,RedesSociales,TiposCapacitaciones
from rest_framework.response import Response
from rest_framework import status
from ..Base.BaseView import ViewPagination, DecoratorPaginateView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db import models

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class AdvertisementsQueryView(APIView):

    def post(self, request, *args, **kwargs):
        results = []
        if ("categoryId" in request.data):
            results = SubCategorySerializersView(SubCategoria.objects.filter_subcategory_has_category(
                request.data["categoryId"]).order_by("-id"), many=True).data

        return Response(results, status.HTTP_200_OK,)


# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AdvertisementView(ViewPagination):

    @DecoratorPaginateView
    def get(self, request, *args, **kwargs):
        meta = None
        subCategory = request.GET.get("subCategoryId", None)
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        if subCategory:
            anuncios = Anuncio.objects.filter_Advertisement_subCategory(
                subCategory)
            anuncio_resulst = anuncios.annotate(user_voted=models.Exists(
                VotoAnuncio.objects.filter(
                    emprendimiento=models.OuterRef("pk"), user=request.user.id)
            ))
            results = AdvertisementSerializersView(anuncio_resulst, many=True)
            return results.data

        anuncios = Anuncio.objects.defer("tipo_capacitacion__userCreate_id", "redes__userUpdate_id", "redes__userCreate_id", "subCategoria__userCreate_id","subCategoria__userUpdate_id","userCreate","userUpdate","subCategoria__categoriaId__userUpdate_id","subCategoria__categoriaId__userCreate_id").select_related(
            "subCategoria", "subCategoria__categoriaId").prefetch_related(models.Prefetch("redes",RedesSociales.objects.all().only("id","name","link")),models.Prefetch("tipo_capacitacion",TiposCapacitaciones.objects.all().only("id","name"))).filter(visible=True).order_by("-id")

        anuncio_resulst = anuncios.annotate(user_voted=models.Exists(
            VotoAnuncio.objects.filter(
                emprendimiento=models.OuterRef("pk"), user=request.user.id)
        ))

        advertisements_serializers = AdvertisementSerializersView(
            anuncio_resulst, many=True, meta=meta)

        return advertisements_serializers.data


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AdvertisementMostVoteView(ViewPagination):

    @DecoratorPaginateView
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        anuncios = Anuncio.objects.defer("tipo_capacitacion__userCreate_id", "redes__userUpdate_id", "redes__userCreate_id", "subCategoria__userCreate_id").select_related(
            "subCategoria", "userCreate", "userUpdate", "subCategoria__categoriaId").prefetch_related("redes", "tipo_capacitacion").filter(visible=True).annotate(nun_votos=models.Count("votoanuncio")).order_by("-nun_votos")[:10]
        

        advertisements_serializers = AdvertisementSerializersView(
            anuncios, many=True, meta=meta)

        return advertisements_serializers.data


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class MyAdvertisementView(ViewPagination):

    @DecoratorPaginateView
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        anuncios = Anuncio.objects.defer("tipo_capacitacion__userCreate_id", "redes__userUpdate_id", "redes__userCreate_id", "subCategoria__userCreate_id").select_related(
            "subCategoria", "userCreate", "userUpdate", "subCategoria__categoriaId").prefetch_related("redes", "tipo_capacitacion").filter(visible=True, userCreate=request.user.id)

        advertisements_serializers = AdvertisementSerializersView(
            anuncios, many=True, meta=meta)

        return advertisements_serializers.data


class SaveAdvertisementView(APIView):

    def post(self, request, *args, **kwargs):
        data = AdvertisementSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Success", status.HTTP_200_OK)

        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class SaveAdvertisementVoto(APIView):

    def post(self, request, *args, **kwargs):

        emprendimiento: int = request.data.get("emprendimiento")
        serializers = AdvertisementVotoSerializers(
            data={"emprendimiento": emprendimiento, "user": request.user.id})

        if serializers.is_valid():
            serializers.save()
            return Response("Success", status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def bulk_delete(self, ids):
        try:
            resulstForDelete = Anuncio.objects.filter(pk__in=ids)
            for _, instance in enumerate(resulstForDelete):
                instance.visible = False

            Anuncio.objects.bulk_update(resulstForDelete, ["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Anuncio {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = AdvertisementSerializers(
                instanceOrNone, data={"visible": False}, partial=True)
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete",  status.HTTP_400_BAD_REQUEST)
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
        return Response("Delete Success", status.HTTP_200_OK)
