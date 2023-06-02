from rest_framework.views import APIView
from ...serializers.pqrs.tipo_serializers import PqrsTipoSerializers
from ....models.models import TipoPqrs
from rest_framework.response import Response
from rest_framework import status


class TipoPqrsView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]
        data = PqrsTipoSerializers(
            TipoPqrs.objects.filter(visible=True).order_by("-id"), many=True, meta=meta)
        return Response(data.data, status.HTTP_200_OK)


class SaveTipoPqrsView(APIView):

    def post(self, request, *args, **kwargs):
        data = PqrsTipoSerializers(data=request.data)

        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK)

        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class DeleteTipoPqrsView(APIView):

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = TipoPqrs.objects.get(pk=pk)
            return seccionId
        except TipoPqrs.DoesNotExist:
            return None
    
    def bulk_delete(self, ids):
        try:
            resulstForDelete = TipoPqrs.objects.filter(pk__in=ids)
            for _,instance in enumerate(resulstForDelete):
                instance.visible = False 

            TipoPqrs.objects.bulk_update(resulstForDelete,["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])
        
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Pqrs tipo {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instance = PqrsTipoSerializers(
                instanceOrNone, data={"visible": False}, partial=True)
            if instance.is_valid():
                instance.save()
            else:
                return Response("Invalid Delete", status.HTTP_200_OK)
            return Response("Delete", status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UpdatePqrsView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            return TipoPqrs.objects.get(pk=pk)
        except TipoPqrs.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Pqrs tipo {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST,)

        instance = PqrsTipoSerializers(instanceOrNone, data=request.data)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)

        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)
