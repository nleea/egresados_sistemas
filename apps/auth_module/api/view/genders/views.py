from ..modules import CreateAPIView, ListAPIView, UpdateAPIView, status, Response,IsAdminRole,DestroyAPIView
from ....models import Genders
from ...serializers.gender.gender_Serializers import GenderSerializers


class GenderListView(ListAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = GenderSerializers(data, many=True)
        return Response(serializers.data, status.HTTP_200_OK)


class GenderCreateView(CreateAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def post(self, request, *args, **kwargs):
        genderSerializers = GenderSerializers(data=request.data)
        if genderSerializers.is_valid():
            genderSerializers.save()
            return Response(genderSerializers.data, status.HTTP_200_OK)
        return Response(genderSerializers.errors, status.HTTP_400_BAD_REQUEST)


class GenderUpdateView(UpdateAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Genders.objects.get(pk=pk)
        except Genders.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        gender = self.get_object()

        if gender is None:
            return Response('Gender Not Found', status.HTTP_400_BAD_REQUEST)

        try:
            genderSerializers = GenderSerializers(gender, data=request.data)
            if genderSerializers.is_valid():
                genderSerializers.update(
                    gender, genderSerializers.validated_data)
                return Response(genderSerializers.data, status.HTTP_200_OK)
            return Response(genderSerializers.errors, status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            return Response( e.args, status.HTTP_400_BAD_REQUEST)

class GendersDestroyView(DestroyAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers
    permission_classes = [IsAdminRole]

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Genders.objects.get(id=pk)
        except Genders.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        gender = self.get_object()
        if gender is None:
            return Response('Gender Not Exist', status.HTTP_200_OK)
        gender.delete()
        return Response('Ok', status.HTTP_200_OK)