from rest_framework.views import APIView
from rest_framework.response import Response
from apps.auth_module.models import Faculties 
from rest_framework import status
from apps.auth_module.api.serializers.head_serializers import FacultiesSerializers,FacultiesSerializersView


class FacultiesView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = FacultiesSerializersView(
            Faculties.objects.filter(visible=True), many=True)

        return Response(data.data, status.HTTP_200_OK)


class SaveFacultiesView(APIView):

    def post(self, request, *args, **kwargs):
        data = FacultiesSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class UpdateFacultiesAreaView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Faculties.objects.get(pk=pk)
            return seccionId
        except Faculties.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Faculty {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = FacultiesSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)


class DeleteFacultiesView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]


    def bulk_delete(self, ids):
        try:
            resulstForDelete = Faculties.objects.filter(pk__in=ids)
            for _,instance in enumerate(resulstForDelete):
                instance.visible = False 

            Faculties.objects.bulk_update(resulstForDelete,["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            eventos = Faculties.objects.get(pk=pk)
            return eventos
        except Faculties.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Bad Request", "Faculty {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            return Response("Error", status.HTTP_400_BAD_REQUEST)
        return Response("Delete Success", status.HTTP_200_OK)
