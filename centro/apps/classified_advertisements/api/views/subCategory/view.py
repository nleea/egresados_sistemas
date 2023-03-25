from rest_framework.views import APIView
from ...serializers.subCategory.subCategory_serializers import SubCategorySerializers,SubCategorySerializersView
from ....models.models import SubCategoria
from rest_framework.response import Response
from .....helpers.create_response import create_response
from rest_framework import status

class SubCategoryView(APIView):
    
   
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = SubCategorySerializersView(SubCategoria.objects.all(),many=True,meta=meta)

        response ,code = create_response(status.HTTP_200_OK,"sucess",{"results":data.data})
        return Response(response,code)

        

class SaveSubCategoryView(APIView):
    
    def post(self, request, *args, **kwargs):
        data = SubCategorySerializers(data=request.data)

        if data.is_valid():
            data.save(userCreate=request.user)
            response,code=create_response(status.HTTP_200_OK,"Success","Sucess")
            return Response(response,code)

        response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",data.errors)
        return Response(response,code)

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
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Sub Categoria {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)

        instance = SubCategorySerializers(instanceOrNone,data=request.data,partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            response, code = create_response(status.HTTP_200_OK,"Success","Success")
            return Response(response,code)

        response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request", instance.errors)
        return Response(response,code)



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


    def delete(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Sub Categoria {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request", "Error")

        response,code = create_response(status.HTTP_200_OK,"Sucess", "Delete Success")
        return Response(response,code)