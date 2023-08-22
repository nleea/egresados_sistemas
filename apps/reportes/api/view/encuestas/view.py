from rest_framework.views import APIView
from apps.auth_module.models import User
from rest_framework.response import Response
from rest_framework import status
from apps.encuestas.models import Question, AnswerUser
from django.db.models import Count, Avg


class ReportesUserFaculta(APIView):
    def get(self, request, *args, **kwargs):
        Question.objects.annotate(num=Count("answeruser"),a=Avg("answeruser"))

        return Response("Ok", status=status.HTTP_200_OK)
