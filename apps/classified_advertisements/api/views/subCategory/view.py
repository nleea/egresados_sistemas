from rest_framework.views import APIView
from ...serializers.subCategory.subCategory_serializers import SubCategorySerializers, SubCategorySerializersView
from ....models.models import SubCategoria
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator 
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')  
class SubCategoryView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = SubCategorySerializersView(
            SubCategoria.objects.select_related("categoriaId","userUpdate","userCreate").filter(visible=True), many=True, meta=meta)
        return Response(data.data, status.HTTP_200_OK)


class SaveSubCategoryView(APIView):

    def post(self, request, *args, **kwargs):
        data = SubCategorySerializers(data=request.data)

        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateSubCategoryView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            subCategoria = SubCategoria.objects.get(pk=pk)
            return subCategoria
        except SubCategoria.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Sub Categoria {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = SubCategorySerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)

        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


class DeleteSubCategoryView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            subCategoria = SubCategoria.objects.get(pk=pk)
            return subCategoria
        except SubCategoria.DoesNotExist:
            return None
    

    def bulk_delete(self, ids):
        try:
            resulstForDelete = SubCategoria.objects.filter(pk__in=ids)
            resulstForDelete._raw_delete(resulstForDelete.db)#type: ignore
            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Sub Categoria {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = SubCategorySerializers(
            instanceOrNone, data=request.data, partial=True)
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete", status.HTTP_400_BAD_REQUEST)
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)

        return Response("Delete Success", status.HTTP_200_OK)
