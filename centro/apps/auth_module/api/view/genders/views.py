from ..modules import CreateAPIView, ListAPIView, UpdateAPIView, status, Response
from ....models import Genders
from ...serializers.gender.gender_Serializers import GenderSerializers


class GenderListView(ListAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = GenderSerializers(data, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class GenderCreateView(CreateAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def post(self, request, *args, **kwargs):
        genderSerializers = GenderSerializers(data=request.data)
        if genderSerializers.is_valid():
            genderSerializers.save()
            return Response(genderSerializers.data, status=status.HTTP_200_OK)
        return Response(genderSerializers.errors, status=status.HTTP_400_BAD_REQUEST)


class GenderUpdateView(UpdateAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return Genders.objects.get(pk=pk)
        except Genders.DoesNotExist:
            raise Response({'message': 'Not Found'},
                           status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        gender = self.get_object()
        genderSerializers = GenderSerializers(gender, data=request.data)
        if genderSerializers.is_valid():
            genderSerializers.save()
            return Response(genderSerializers.data, status=status.HTTP_200_OK)
        return Response(genderSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
