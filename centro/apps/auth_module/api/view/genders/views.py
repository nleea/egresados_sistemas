from gc import get_referents
from ..modules import CreateAPIView, ListAPIView, UpdateAPIView, status, Response, create_response
from ....models import Genders
from ...serializers.gender.gender_Serializers import GenderSerializers


class GenderListView(ListAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = GenderSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, serializers.data)
        return Response(response, status=code)


class GenderCreateView(CreateAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def post(self, request, *args, **kwargs):
        genderSerializers = GenderSerializers(data=request.data)
        if genderSerializers.is_valid():
            genderSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, genderSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, genderSerializers.errors)
        return Response(response, status=code)


class GenderUpdateView(UpdateAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return Genders.objects.get(pk=pk)
        except Genders.DoesNotExist:
            response, code = create_response(
                status.HTTP_200_OK, 'No Found')
            raise Response(response,
                           status=code)

    def put(self, request, *args, **kwargs):
        gender = self.get_object()
        genderSerializers = GenderSerializers(gender, data=request.data)
        if genderSerializers.is_valid():
            genderSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, genderSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, genderSerializers.errors)
        return Response(response, status=code)
