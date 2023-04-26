from rest_framework.views import APIView
from ...serializers.questions.questions_serializers import QuestionSerializers, QuestionSerializersUpate
from ....models.models import Question
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator 

@method_decorator(cache_page(60 * 5), name='dispatch') 
class QuestionsView(APIView):

    def get(self, request, *args, **kwargs):
        data = QuestionSerializers(Question.objects.all(), many=True)
        return Response(data.data, status.HTTP_200_OK)


class SaveQuestionsView(APIView):

    def post(self, request, *args, **kwargs):
        data = QuestionSerializers(data=request.data)

        if data.is_valid():
            data.save(momento=request.data["momento"], userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK)
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class DeleteQuestionsView(APIView):

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Question.objects.get(pk=pk)
            return seccionId
        except Question.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Questions {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)
        try:
            instanceOrNone.delete()
            return Response("Delete", status.HTTP_200_OK)
        except BaseException as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UpdateQuestionsView(APIView):

    def _allowed_methods(self):
        self.http_method_names.append("put")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Question.objects.get(pk=pk)
            return seccionId
        except Question.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response("Questions {} not exist".format(self.kwargs.get('pk')), status.HTTP_400_BAD_REQUEST)

        instance = QuestionSerializersUpate(
            instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)
