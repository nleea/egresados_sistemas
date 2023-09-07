from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.encuestas.models import Question, Answer
from django.db.models import (
    Count,
    F,
    ExpressionWrapper,
    FloatField,
    Q,
)


class ReportesUserFaculta(APIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.defer(
            "momento", "depende_respuesta", "userCreate", "userUpdate"
        ).annotate(
            total_users=Count("answeruser", filter=Q(answeruser__pregunta=F("pk")))
        )

        response_info = []

        for question in questions:
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

            response_info_question = []

            for answer in answers:
                faculty_info = {
                    "name": answer.faculty_name,
                    "porcentaje": answer.faculty_percentage,
                    "cantidad_usuarios": answer.faculty_total_users,
                }

                answer_info = {
                    "respuestas": answer.respuesta,
                    "porcentaje": answer.faculty_percentage,
                    "facultades": [faculty_info],
                }

                existing_answer_info = next(
                    (
                        item
                        for item in response_info_question
                        if item["respuestas"] == answer_info["respuestas"]
                    ),
                    None,
                )

                if existing_answer_info:
                    existing_answer_info["porcentaje"] += faculty_info["porcentaje"]
                    existing_answer_info["facultades"].append(faculty_info)
                else:
                    response_info_question.append(answer_info)

            question_info = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": response_info_question,
            }

            response_info.append(question_info)

        return Response(response_info, status=status.HTTP_200_OK)


class ReportesUserFacultaWith(APIView):
    def get_facultad(self):
        questions = (
            Question.objects.defer(
                "momento", "depende_respuesta", "userCreate", "userUpdate"
            )
            .annotate(total_users=Count("answeruser"))
            .all()
        )
        F_SUB = "answeruser__user__persons__program__faculty__name"

        answers = (
            Answer.objects.defer(
                "userCreate",
                "userUpdate",
                "pregunta__momento",
                "pregunta__userCreate",
                "pregunta__userUpdate",
                "pregunta__depende_respuesta",
            )
            .select_related("pregunta")
            .annotate(
                num_users=Count("answeruser"),
                faculty_name=F(F_SUB),
                faculty_total_users=Count(
                    "answeruser",
                    filter=Q(faculty_name=F(F_SUB)),
                ),
                total_users=Count(
                    "answeruser", filter=Q(answeruser__pregunta=F("pregunta__pk"))
                ),
            )
            .all()
        )

        response_info = []

        for question in questions:
            question_info = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": [],
            }

            answer_question = list(
                filter(lambda x: x.pregunta_id == question.pk, answers)
            )

            for i in answer_question:
                answer_info = {
                    "faculta": i.faculty_name,
                    "total": i.faculty_total_users,
                    "porcentaje": (i.faculty_total_users / question.total_users) * 100
                    if question.total_users != 0
                    else 0,
                }
                valid = True
                for index, x in enumerate(question_info["respuestas"]):
                    if x["faculta"] == i.faculty_name:
                        info_dict = question_info["respuestas"][index]
                        answer_info_update = {
                            "faculta": x["faculta"],
                            "total": info_dict["total"] + i.faculty_total_users,
                            "porcentaje": (
                                (info_dict["total"] + i.faculty_total_users)
                                / question.total_users
                            )
                            * 100
                            if question.total_users != 0
                            else 0,
                        }

                        question_info["respuestas"][index] = answer_info_update
                        valid = False
                if valid:
                    question_info["respuestas"].append(answer_info)

            response_info.append(question_info)
        return response_info

    def get_programa(self):
        questions = (
            Question.objects.defer(
                "momento", "depende_respuesta", "userCreate", "userUpdate"
            )
            .annotate(total_users=Count("answeruser"))
            .all()
        )
        F_SUB = "answeruser__user__persons__program__name"

        answers = (
            Answer.objects.defer(
                "userCreate",
                "userUpdate",
                "pregunta__momento",
                "pregunta__userCreate",
                "pregunta__userUpdate",
                "pregunta__depende_respuesta",
            )
            .select_related("pregunta")
            .annotate(
                num_users=Count("answeruser"),
                program__name=F(F_SUB),
                program_total_users=Count(
                    "answeruser",
                    filter=Q(program__name=F(F_SUB)),
                ),
                total_users=Count(
                    "answeruser", filter=Q(answeruser__pregunta=F("pregunta__pk"))
                ),
            )
            .all()
        )

        response_info = []

        for question in questions:
            question_info = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": [],
            }

            answer_question = list(
                filter(lambda x: x.pregunta_id == question.pk, answers)
            )

            for i in answer_question:
                answer_info = {
                    "programa": i.program__name,
                    "total": i.program_total_users,
                    "porcentaje": (i.program_total_users / question.total_users) * 100
                    if question.total_users != 0
                    else 0,
                }
                valid = True
                for index, x in enumerate(question_info["respuestas"]):
                    if x["programa"] == i.program__name:
                        info_dict = question_info["respuestas"][index]
                        answer_info_update = {
                            "programa": x["programa"],
                            "total": info_dict["total"] + i.program_total_users,
                            "porcentaje": (
                                (info_dict["total"] + i.program_total_users)
                                / question.total_users
                            )
                            * 100
                            if question.total_users != 0
                            else 0,
                        }

                        question_info["respuestas"][index] = answer_info_update
                        valid = False
                if valid:
                    question_info["respuestas"].append(answer_info)

            response_info.append(question_info)
        return response_info

    def get_programa_facultad(self, facultad):
        questions = (
            Question.objects.defer(
                "momento", "depende_respuesta", "userCreate", "userUpdate"
            )
            .filter(answeruser__user__persons__program__faculty=facultad)
            .annotate(total_users=Count("answeruser"))
        )
        F_SUB = "answeruser__user__persons__program__name"

        answers = (
            Answer.objects.defer(
                "userCreate",
                "userUpdate",
                "pregunta__momento",
                "pregunta__userCreate",
                "pregunta__userUpdate",
                "pregunta__depende_respuesta",
            )
            .select_related("pregunta")
            .filter(answeruser__user__persons__program__faculty=facultad)
            .annotate(
                num_users=Count("answeruser"),
                program__name=F(F_SUB),
                program_total_users=Count(
                    "answeruser",
                    filter=Q(program__name=F(F_SUB)),
                ),
                total_users=Count(
                    "answeruser", filter=Q(answeruser__pregunta=F("pregunta__pk"))
                ),
            )
        )

        response_info = []

        for question in questions:
            question_info = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": [],
            }

            answer_question = list(
                filter(lambda x: x.pregunta_id == question.pk, answers)
            )

            for i in answer_question:
                answer_info = {
                    "programa": i.program__name,
                    "total": i.program_total_users,
                    "porcentaje": (i.program_total_users / question.total_users) * 100
                    if question.total_users != 0
                    else 0,
                }
                valid = True
                for index, x in enumerate(question_info["respuestas"]):
                    if x["programa"] == i.program__name:
                        info_dict = question_info["respuestas"][index]
                        answer_info_update = {
                            "programa": x["programa"],
                            "total": info_dict["total"] + i.program_total_users,
                            "porcentaje": (
                                (info_dict["total"] + i.program_total_users)
                                / question.total_users
                            )
                            * 100
                            if question.total_users != 0
                            else 0,
                        }

                        question_info["respuestas"][index] = answer_info_update
                        valid = False
                if valid:
                    question_info["respuestas"].append(answer_info)

            response_info.append(question_info)
        return response_info

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get("filter") == "facultad":
                f2 = kwargs.get("facultad", None)
                if f2:
                    response_info = self.get_programa_facultad(int(f2))
                    return Response(response_info)

                response_info = self.get_facultad()
                return Response(response_info)
            else:
                response_info = self.get_programa()
                return Response(response_info)

        except Exception as e:
            return Response({"error": e.args}, status=status.HTTP_404_NOT_FOUND)
