from rest_framework.views import APIView
from rest_framework.response import Response
from apps.auth_module.api.serializers.head_serializers import ProgramsSerializers,ProgramsSerializersView
from apps.auth_module.models import Programs
from rest_framework import status


class ProgramsView(APIView):

    def get(self, request, *args, **kwargs):
        meta = None
        if 'meta' in request.headers:
            meta = request.headers["meta"]

        data = ProgramsSerializersView(
            Programs.objects.filter(visible=True), many=True)

        return Response(data.data, 200)


class SaveProgramsView(APIView):

    def post(self, request, *args, **kwargs):
        data = ProgramsSerializers(data=request.data)
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Success", 200)
        return Response(data.errors, 400)


class UpdateProgramsView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Programs.objects.get(pk=pk)
            return seccionId
        except Programs.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Programs {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = ProgramsSerializers(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", 200)
        return Response(instance.errors, 400)


class DeleteProgramsView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("delete")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]


    def bulk_delete(self, ids):
        try:
            resulstForDelete = Programs.objects.filter(pk__in=ids)
            for _,instance in enumerate(resulstForDelete):
                instance.visible = False 

            Programs.objects.bulk_update(resulstForDelete,["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            eventos = Programs.objects.get(pk=pk)
            return eventos
        except Programs.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):

        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Programs {} not exist".format(self.kwargs.get('pk')), 400)

        try:
            instanceOrNone.delete()
        except instanceOrNone.DoesNotExist:
            return Response("Error", 400)
        return Response("Delete Success", 200)
