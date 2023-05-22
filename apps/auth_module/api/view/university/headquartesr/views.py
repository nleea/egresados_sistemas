from rest_framework.views import APIView
from rest_framework.response import Response
from apps.auth_module.api.serializers.head_serializers import HeadSerializers
from apps.auth_module.models import Headquarters
from rest_framework import status


class HeadquartersView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = HeadSerializers(
            Headquarters.objects.filter(visible=True), many=True)

        return Response(data.data, status.HTTP_200_OK)


class SaveHeadquartersView(APIView):

    def post(self, request, *args, **kwargs):
        data = HeadSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateHeadquartersView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Headquarters.objects.get(pk=pk)
            return seccionId
        except Headquarters.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Headquarters {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = HeadSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


class DeleteHeadquartersView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def bulk_delete(self, ids):
        try:
            resulstForDelete = Headquarters.objects.filter(pk__in=ids)
            for _,instance in enumerate(resulstForDelete):
                instance.visible = False 

            Headquarters.objects.bulk_update(resulstForDelete,["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            eventos = Headquarters.objects.get(pk=pk)
            return eventos
        except Headquarters.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Headquarters {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
        return Response("Delete Success", status.HTTP_200_OK)
