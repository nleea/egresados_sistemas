from rest_framework.views import APIView
from apps.auth_module.models import User
from rest_framework.response import Response
from rest_framework import status
from apps.encuestas.models import Question, AnswerUser
from django.db.models import Count, Avg, F, ExpressionWrapper, FloatField
from apps.reportes.api.serializers.questions_serializers import ReporteSerializersView


class ReportesUserFaculta(APIView):
    def get(self, request, *args, **kwargs):
        # questions = Question.objects.annotate(
        #     num=Count("answeruser"), a=Avg(F("answeruser"))
        # ).select_related("answeruser")

        questions = Question.objects.annotate(
            facultad=F("answeruser__user__persons__program__faculty__name"),
            num=Count("answeruser__user"),
            promedio_respuestas=ExpressionWrapper(
                Count("id") / F("answeruser__user__persons__program__faculty__id"),
                output_field=FloatField(),
            ),
        )

        serializers_data = ReporteSerializersView(questions, many=True)

        return Response(serializers_data.data, status=status.HTTP_200_OK)
