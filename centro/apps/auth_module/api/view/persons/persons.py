from ...serializers.person.persons_serializers import PersonsSerializers
from ....models import Persons
from rest_framework import status
from django.http import Http404
from ..modules import ListAPIView, CreateAPIView, UpdateAPIView, Response, create_response


class PersonView(ListAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = PersonsSerializers(data, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class PersonCreateView(CreateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def post(self, request, *args, **kwargs):
        personSerializers = PersonsSerializers(data=request.data)
        if personSerializers.is_valid():
            personSerializers.save()
            return Response(personSerializers.data, status=status.HTTP_200_OK)
        return Response(personSerializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonUpdateView(UpdateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def get_object(self):
        try:
            pk = self.request.user.id
            return Persons.objects.filter(user__id=pk)[0]
        except Persons.DoesNotExist:
            raise Http404({'message': 'Person not found'})

    def put(self, request, *args, **kwargs):
        person = self.get_object()
        personSerializers = PersonsSerializers(person, data=request.data)
        if personSerializers.is_valid():
            personSerializers.update()
            return Response(personSerializers.data, status=status.HTTP_200_OK)
        return Response(personSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
