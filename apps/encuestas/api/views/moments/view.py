from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from ...serializers.momento.momento_serializers import MomentSerializers
from ....models.models import TipoMomento
from rest_framework.response import Response
from .....helpers.create_response import create_response
from rest_framework import status
from ..BaseView import BaseView

class MomentView(BaseView):
       
    def get(self, request, *args, **kwargs):
        data = MomentSerializers(TipoMomento.objects.all(),many=True,meta=self.get_meta())
        response ,code = create_response(status.HTTP_200_OK,"sucess",{"results":data.data})
        return Response(response,code)


class SaveMomentsView(APIView):

    def post(self, request, *args, **kwargs):
        data = MomentSerializers(data=request.data)

        if data.is_valid():
            data.save(userCreate=request.user)
            response,code=create_response(status.HTTP_200_OK,"Success","Sucess")
            return Response(response,code)

        response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",data.errors)
        return Response(response,code)


class DeleteMomentsView(BaseView):
    
    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = TipoMomento.objects.get(pk=pk)
            return seccionId
        except TipoMomento.DoesNotExist:
            return None
    

    def delete(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Momento {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)
        
        try:
            instanceOrNone.delete()
            response,code = create_response(status.HTTP_200_OK,"Success","Delete" )
            return Response(response,code)
        except BaseException as e:
            response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",e.args )
            return Response(response,code)



class UpdateMomentsView(BaseView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = TipoMomento.objects.get(pk=pk)
            return seccionId
        except TipoMomento.DoesNotExist:
            return None


    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Momento {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)

        instance = MomentSerializers(instanceOrNone,data=request.data,partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            response, code = create_response(status.HTTP_200_OK,"Success","Success")
            return Response(response,code)

        response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request", instance.errors)
        return Response(response,code)
