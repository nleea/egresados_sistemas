from rest_framework.views import APIView
from apps.auth_module.models import User, Faculties, Programs
from rest_framework.response import Response
from rest_framework import status
from apps.encuestas.models import Question, AnswerUser, Answer
from django.db.models import (
    Count,
    Avg,
    F,
    ExpressionWrapper,
    FloatField,
    Prefetch,
    Subquery,
    OuterRef,
    Q,
)
from apps.reportes.api.serializers.questions_serializers import (
    ReporteSerializersView,
    QuestionSerializersViewd,
)


class ReportesUserFaculta(APIView):
    def get_faculty_percentage(self, answer, faculty, count):
        total_answer_users = (
            AnswerUser.objects.filter(
                respuesta=answer,
                pregunta=answer.pregunta,
                user__persons__program__faculty__id=faculty,
            )
            .defer("userCreate", "userUpdate")
            .select_related(
                "respuesta", "pregunta", "user", "user__persons__program__faculty"
            )
            .count()
        )

        if total_answer_users == 0:
            return 0

        faculty_percentage = (total_answer_users / count) * 100
        return faculty_percentage

    def get_question_with_answers(self, question_id):
        question = Question.objects.get(id=question_id)
        answers = (
            Answer.objects.filter(pregunta__pk=question.pk)
            .defer("userCreate", "userUpdate")
            .select_related("pregunta")
        )

        response_data = {"pregunta": question.pregunta_nombre, "respuestas": []}
        faculties = Faculties.objects.all().values("id", "name")

        for answer in answers:
            answer_data = {"respuesta": answer.respuesta, "facultades": []}
            count = (
                AnswerUser.objects.filter(pregunta=answer.pregunta)
                .defer("userCreate", "userUpdate", "user")
                .select_related("respuesta", "pregunta")
                .count()
            )
            for faculty in faculties:
                porcentaje = self.get_faculty_percentage(answer, faculty["id"], count)
                answer_data["facultades"].append(
                    {"name": faculty["name"], "porcentaje": porcentaje}
                )

            response_data["respuestas"].append(answer_data)

        return response_data

    def get(self, request, *args, **kwargs):
        data = self.get_question_with_answers(1)

        return Response(data, status=status.HTTP_200_OK)
