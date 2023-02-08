from rest_framework.views import APIView
from ...serializers.respuesta.respuesta_serializers import RespuestaSerializers
from ....models.models import Respuesta
from rest_framework.response import Response
from .....helpers.create_response import create_response
from rest_framework import status

class RespuestaView(APIView):
   
    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = RespuestaSerializers(Respuesta.objects.all(),many=True,meta=meta)
        response ,code = create_response(status.HTTP_200_OK,"sucess",{"results":data.data})
        return Response(response,code)


class SaveRespuestaView(APIView):

    def post(self, request, *args, **kwargs):
        data = RespuestaSerializers(data=request.data)

        if data.is_valid():
            data.save(anexo=request.data["anexo"],pqrs=request.data["pqrs"], userCreate=request.user)
            response,code=create_response(status.HTTP_200_OK,"Success","Sucess")
            return Response(response,code)

        response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request",data.errors)
        return Response(response,code)


class UpdateRespuestaView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Respuesta.objects.get(pk=pk)
            return seccionId
        except Respuesta.DoesNotExist:
            return None


    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            response, code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request","Respuesta {} not exist".format(self.kwargs.get('pk')))
            return Response(response,code)

        instance = RespuestaSerializers(instanceOrNone,data=request.data)
        if instance.is_valid():
            instance.save(anexo=request.data["anexo"],userUpdate=request.user)
            response, code = create_response(status.HTTP_200_OK,"Success","Success")
            return Response(response,code)

        response,code = create_response(status.HTTP_400_BAD_REQUEST,"Bad Request", instance.errors)
        return Response(response,code)
