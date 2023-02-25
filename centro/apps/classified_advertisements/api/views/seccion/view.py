from rest_framework.views import APIView
from ...serializers.seccion.seccion_serializers import SeccionSerializers
from ...serializers.category.category_serializers import CategorySerializers
from ...serializers.subCategory.subCategory_serializers import SubCategorySerializers
from ...serializers.advertissement.advertisement_serialziers import AdvertisementSerializers
from ....models.models import Seccion,Categoria,Anuncio,SubCategoria
from rest_framework.response import Response
from .....helpers.create_response import create_response
from rest_framework import status

class SeccionView(APIView):
   
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = SeccionSerializers(Seccion.objects.all(),many=True,meta=meta)
        response ,code = create_response(status.HTTP_200_OK,"sucess",{"results":data.data})
        return Response(response,code)


class SaveSeccionView(APIView):

    def post(self, request, *args, **kwargs):
        data = SeccionSerializers(data=request.data)

        if data.is_valid():
            data.save(userCreate=request.user)
            response,code=create_response(status.HTTP_200_OK,"Success","Sucess")
            return Response(response,code)

        response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",data.errors)
        return Response(response,code)


class UpdateSeccionView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
    
    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Seccion.objects.get(pk=pk)
            return seccionId
        except Seccion.DoesNotExist:
            return None

    
    def put(self, request, *args, **kwargs):
        
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Seccion {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)

        instance = SeccionSerializers(instanceOrNone,data=request.data)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            response, code = create_response(status.HTTP_200_OK,"Success","Success")
            return Response(response,code)

        response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request", instance.errors)
        return Response(response,code)


class DeleteSeccionView(APIView):
    
    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Seccion.objects.get(pk=pk)
            return seccionId
        except Seccion.DoesNotExist:
            return None

    def delete(self,request,*args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Seccion {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)

        try:
            instanceOrNone.delete()
            response,code = create_response(status.HTTP_200_OK,"Success","Delete" )
            return Response(response,code)
        except BaseException as e:
            response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",e.args )
            return Response(response,code)


class ApiQueryView(APIView):
    
    def post(self, request, *args, **kwargs):
        if request.data['type'] == "categorias":
            response = CategorySerializers(Categoria.objects.filter(seccionId=request.data["id"]),many=True)
            response ,code = create_response(status.HTTP_200_OK,"sucess",{"results":response.data})
            return Response(response,code)
        if request.data['type'] == "subCategorias":
            response = SubCategorySerializers(SubCategoria.objects.filter(categoriId=request.data["id"]),many=True)
            response ,code = create_response(status.HTTP_200_OK,"sucess",{"results":response.data})
            return Response(response,code)
        if request.data['type'] == "anuncios":
            response = AdvertisementSerializers(Anuncio.objects.filter(subCategori=request.data["id"]),many=True)
            response ,code = create_response(status.HTTP_200_OK,"sucess",{"results":response.data})
            return Response(response,code)
        
        response ,code = create_response(status.HTTP_200_OK,"sucess",{"results":"Error not match"})
        return Response(response,code)