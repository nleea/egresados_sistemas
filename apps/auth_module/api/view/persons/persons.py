from ...serializers.person.persons_serializers import PersonsSerializers, PersonsSimpleSerializers
from ....models import Persons
from rest_framework import status
from ..modules import ListAPIView, CreateAPIView, UpdateAPIView, Response
from rest_framework.views import APIView
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class PersonView(ListAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def get(self, request, *args, **kwargs):
        data = Persons.objects.select_related(
            "user").get(user__id=request.user.id)
        serializers = PersonsSerializers([data], many=True)
        return Response(serializers.data, status.HTTP_200_OK)


class PersonCreateView(CreateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSimpleSerializers

    def post(self, request, *args, **kwargs):
        personSerializers = PersonsSimpleSerializers(data=request.data)
        if personSerializers.is_valid():
            personSerializers.save()
            return Response(personSerializers.data, status.HTTP_200_OK)
        return Response(personSerializers.errors, status.HTTP_400_BAD_REQUEST)


class PersonUpdateView(APIView):

    def get_object(self):
        try:
            pk = self.request.user.pk
            return Persons.objects.get(user__id=pk)
        except Persons.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        person = self.get_object()

        if person is None:
            # type: ignore
            return Response("person {} don't exist", status.HTTP_400_BAD_REQUEST)
        try:
            personSerializers = PersonsSimpleSerializers(
                person, data=request.data, partial=True)
            if personSerializers.is_valid():
                personSerializers.save()
                return Response("Success", status.HTTP_200_OK)
            return Response(personSerializers.error_messages, status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)
