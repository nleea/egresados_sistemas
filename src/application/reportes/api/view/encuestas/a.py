from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.application.encuestas.models import Question, AnswerUser, Answer
from django.db.models import (
    Count,
    F,
    ExpressionWrapper,
    FloatField,
    Q,
)


class ReportesUserFaculta(APIView):
    def get_question_info(self, question_pk):
        try:
            question = (
                Question.objects.defer(
                    "momento", "depende_respuesta", "userCreate", "userUpdate"
                )
                .annotate(
                    total_users=Count(
                        "answeruser", filter=Q(answeruser__pregunta=question_pk)
                    )
                )
                .get(pk=question_pk)
            )

            F_SUB = "answeruser__user__persons__program__faculty__name"

            answers = (
                Answer.objects.filter(pregunta=question.pk)
                .defer("userCreate", "userUpdate", "pregunta")
                .annotate(
                    num_users=Count("answeruser"),
                    faculty_name=F(F_SUB),
                    faculty_total_users=Count(
                        "answeruser",
                        filter=Q(faculty_name=F(F_SUB)),
                    ),
                    faculty_percentage=ExpressionWrapper(
                        (F("num_users") / question.total_users) * 100,
                        output_field=FloatField(),
                    ),
                )
            )

            response_info = []

            for answer in answers:
                faculty_info = {
                    "name": answer.faculty_name,
                    "porcentaje": answer.faculty_percentage,
                    "cantidad_usuarios": answer.faculty_total_users,
                }

                answer_info = {
                    "respuestas": answer.respuesta,
                    "facultades": [faculty_info],
                }

                existing_answer_info = next(
                    (
                        item
                        for item in response_info
                        if item["respuestas"] == answer_info["respuestas"]
                    ),
                    None,
                )

                if existing_answer_info:
                    existing_answer_info["facultades"].append(faculty_info)
                else:
                    response_info.append(answer_info)

            result = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": response_info,
            }

            return result

        except Question.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        data = self.get_question_info(1)

        return Response(data, status=status.HTTP_200_OK)


class ReportesUser(APIView):
    def get(self, request, *args, **kwargs):
        try:
            question = (
                Question.objects.defer(
                    "momento", "depende_respuesta", "userCreate", "userUpdate"
                )
                .annotate(total_users=Count("answeruser"))
                .get(pk=1)
            )

            answers = (
                Answer.objects.filter(pregunta=question)
                .defer(
                    "userCreate",
                    "userUpdate",
                    "pregunta__momento",
                    "pregunta__userCreate",
                    "pregunta__userUpdate",
                    "pregunta__depende_respuesta",
                )
                .select_related("pregunta")
                .annotate(num_users=Count("answeruser"))
            )
            response_info = []

            for answer in answers:
                users_for_answer = answer.num_users

                percentage = (
                    (users_for_answer / question.total_users) * 100
                    if question.total_users > 0
                    else 0
                )
                answer_info = {
                    "respuesta": answer.respuesta,
                    "cantidad_usuarios": users_for_answer,
                    "porcentaje": percentage,
                }
                response_info.append(answer_info)
            result = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": response_info,
            }

            return Response(result)

        except Question.DoesNotExist:
            return None
