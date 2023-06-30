from rest_framework.views import APIView
from ...serializers.questions.questions_serializers import (
    QuestionSerializers,
    QuestionSerializersView,
    QuestionCreateSerializers
)
from ....models.models import Question, AnswerUser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class QuestionsView(APIView):
    def get(self, request, *args, **kwargs):
        resulst = (
            Question.objects
            .select_related("depende_respuesta", "depende_respuesta__pregunta","momento")
            .prefetch_related("answer_set")
            .filter(visible=True)
        )

        data = QuestionSerializersView(resulst, many=True)

        return Response(data.data, status.HTTP_200_OK)


class SaveQuestionsView(APIView):
    def post(self, request, *args, **kwargs):
        data = QuestionCreateSerializers(data=request.data)
        
        if data.is_valid():
            data.save(userCreate=request.user)
            return Response("Sucess", status.HTTP_200_OK)
       
        return Response(data.errors, status.HTTP_400_BAD_REQUEST)


class SaveQuestionsResponse(APIView):
    def post(self, request, *args, **kwargs):
        try:
            aswer_create = []
            for i in request.data["respuestas"]:
                if i["type"] == "unica respuesta":
                    aswer_create.append(
                        AnswerUser(respuesta_id=i["respuesta"], user=request.user)
                    )
                elif i["type"] == "pregunta corta" or i["type"] == "pregunta larga":
                    aswer_create.append(
                        AnswerUser(pregunta_id=i["pregunta"],texto=i["respuesta"], user=request.user)
                    )
                elif i["type"] == "multiple":
                    for x in i["respuesta"]:
                        aswer_create.append(
                            AnswerUser(respuesta_id=x, user=request.user)
                        )
            
            AnswerUser.objects.bulk_create(aswer_create)

            return Response("Exitoso", status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class DeleteQuestionsView(APIView):
    def get_object(self):
        try:
            pk = self.kwargs.get("pk")
            seccionId = Question.objects.get(pk=pk)
            return seccionId
        except Question.DoesNotExist:
            return None

    def bulk_delete(self, ids):
        try:
            resulstForDelete = Question.objects.filter(pk__in=ids)
            for _, instance in enumerate(resulstForDelete):
                instance.visible = False

            Question.objects.bulk_update(resulstForDelete, ["visible"])

            return Response("Success", 200)
        except Exception as e:
            return Response(e.args, 400)

    def delete(self, request, *args, **kwargs):
        if "ids" in request.data:
            return self.bulk_delete(request.data["ids"])

        instanceOrNone = self.get_object()
        if instanceOrNone is None:
            return Response(
                "Questions {} not exist".format(self.kwargs.get("pk")),
                status.HTTP_400_BAD_REQUEST,
            )
        try:
            instance = QuestionSerializers(
                instanceOrNone, data={"visible": False}, partial=True
            )
            if instance.is_valid():
                instance.save(userUpdate=request.user)
            else:
                return Response("Invalid Delete", status.HTTP_400_BAD_REQUEST)
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
            return Response(
                "Questions {} not exist".format(self.kwargs.get("pk")),
                status.HTTP_400_BAD_REQUEST,
            )

        instance = QuestionSerializers(instanceOrNone, data=request.data, partial=True)
        if instance.is_valid():
            instance.save(userUpdate=request.user)
            return Response("Success", status.HTTP_200_OK)
        return Response(instance.errors, status.HTTP_400_BAD_REQUEST)
