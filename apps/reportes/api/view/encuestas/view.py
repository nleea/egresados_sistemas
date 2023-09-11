from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.encuestas.models import Question, Answer
from django.db.models import (
    Count,
    F,
    Q,
)
import pandas as pd
import io
import xlsxwriter
from django.http import HttpResponse


class ReportesUserFacultaAndPrograma(APIView):
    def get_user_facultad(self):
        questions = Question.objects.defer(
            "momento", "depende_respuesta", "userCreate", "userUpdate"
        ).annotate(
            total_users=Count("answeruser", filter=Q(answeruser__pregunta=F("pk")))
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
            response_info_question = []

            answer_question = list(
                filter(lambda x: x.pregunta_id == question.pk, answers)
            )

            for answer in answer_question:
                faculty_info = {
                    "name": answer.faculty_name,
                    "porcentaje": (answer.faculty_total_users / question.total_users)
                    * 100
                    if question.total_users != 0
                    else 0,
                    "cantidad_usuarios": answer.faculty_total_users,
                }

                answer_info = {
                    "respuestas": answer.respuesta,
                    "porcentaje": (answer.faculty_total_users / question.total_users)
                    * 100
                    if question.total_users != 0
                    else 0,
                    "num_usuarios": answer.num_users,
                    "data": [],
                }

                if faculty_info["name"] != None:
                    answer_info["data"] = [faculty_info]

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
                    existing_answer_info["num_usuarios"] += answer.num_users
                    existing_answer_info["data"].append(faculty_info)
                else:
                    response_info_question.append(answer_info)

            question_info = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": response_info_question,
            }

            response_info.append(question_info)
        return response_info

    def get_user_programa_facultad(self, facultad):
        questions = Question.objects.defer(
            "momento", "depende_respuesta", "userCreate", "userUpdate"
        ).annotate(
            total_users=Count(
                "answeruser",
                filter=Q(answeruser__user__persons__program__faculty=facultad),
            )
        )

        response_info = []
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

        for question in questions:
            response_info_question = []

            answer_question = list(
                filter(lambda x: x.pregunta_id == question.pk, answers)
            )

            for answer in answer_question:
                faculty_info = {
                    "name": answer.program__name,
                    "porcentaje": (answer.program_total_users / question.total_users)
                    * 100
                    if question.total_users != 0
                    else 0,
                    "cantidad_usuarios": answer.program_total_users,
                }

                answer_info = {
                    "respuestas": answer.respuesta,
                    "porcentaje": (answer.program_total_users / question.total_users)
                    * 100
                    if question.total_users != 0
                    else 0,
                    "num_usuarios": answer.num_users,
                    "data": [],
                }

                if faculty_info["name"] != None:
                    answer_info["data"] = [faculty_info]

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
                    existing_answer_info["num_usuarios"] += answer.num_users
                    existing_answer_info["data"].append(faculty_info)
                else:
                    response_info_question.append(answer_info)

            question_info = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": response_info_question,
            }

            response_info.append(question_info)
        return response_info

    def get_user_programa(self):
        questions = Question.objects.defer(
            "momento", "depende_respuesta", "userCreate", "userUpdate"
        ).annotate(
            total_users=Count("answeruser", filter=Q(answeruser__pregunta=F("pk")))
        )

        response_info = []
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

        for question in questions:
            response_info_question = []

            answer_question = list(
                filter(lambda x: x.pregunta_id == question.pk, answers)
            )

            for answer in answer_question:
                faculty_info = {
                    "name": answer.program__name,
                    "porcentaje": (answer.program_total_users / question.total_users)
                    * 100
                    if question.total_users != 0
                    else 0,
                    "cantidad_usuarios": answer.program_total_users,
                }

                answer_info = {
                    "respuestas": answer.respuesta,
                    "porcentaje": (answer.program_total_users / question.total_users)
                    * 100
                    if question.total_users != 0
                    else 0,
                    "num_usuarios": answer.num_users,
                    "data": [],
                }

                if faculty_info["name"] != None:
                    answer_info["data"] = [faculty_info]

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
                    existing_answer_info["num_usuarios"] += answer.num_users
                    existing_answer_info["data"].append(faculty_info)
                else:
                    response_info_question.append(answer_info)

            question_info = {
                "pregunta": question.pregunta_nombre,
                "total": question.total_users,
                "respuestas": response_info_question,
            }

            response_info.append(question_info)
        return response_info

    def get(self, request, *args, **kwargs):
        if kwargs.get("filter") == "facultad":
            facultad = kwargs.get("facultad", None)
            if facultad:
                response_info = self.get_user_programa_facultad(int(facultad))
                return Response(response_info, status=status.HTTP_200_OK)
            response_info = self.get_user_facultad()
            return Response(response_info, status=status.HTTP_200_OK)
        elif kwargs.get("filter") == "programa":
            response_info = self.get_user_programa()
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
                    "name": i.faculty_name,
                    "total": i.faculty_total_users,
                    "porcentaje": (i.faculty_total_users / question.total_users) * 100
                    if question.total_users != 0
                    else 0,
                }
                valid = True
                for index, x in enumerate(question_info["respuestas"]):
                    if x["name"] == i.faculty_name:
                        info_dict = question_info["respuestas"][index]
                        answer_info_update = {
                            "name": x["name"],
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
                    "name": i.program__name,
                    "total": i.program_total_users,
                    "porcentaje": (i.program_total_users / question.total_users) * 100
                    if question.total_users != 0
                    else 0,
                }
                valid = True
                for index, x in enumerate(question_info["respuestas"]):
                    if x["name"] == i.program__name:
                        info_dict = question_info["respuestas"][index]
                        answer_info_update = {
                            "name": x["name"],
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
            .annotate(
                total_users=Count(
                    "answeruser",
                    filter=Q(answeruser__user__persons__program__faculty=facultad),
                )
            )
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
                    "name": i.program__name,
                    "total": i.program_total_users,
                    "porcentaje": (i.program_total_users / question.total_users) * 100
                    if question.total_users != 0
                    else 0,
                }
                valid = True
                for index, x in enumerate(question_info["respuestas"]):
                    if x["name"] == i.program__name:
                        info_dict = question_info["respuestas"][index]
                        answer_info_update = {
                            "name": x["name"],
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

    def get_response_excel(self, data):
        new_data = {"pregunta": [], "total": [], "respuestas": []}

        for i in data:
            new_data["pregunta"].append(i["pregunta"])
            new_data["total"].append(i["total"])
            new_data["respuestas"].append(
                i["respuestas"] if len(i["respuestas"]) else []
            )

        df = pd.DataFrame(new_data)
        for i in range(df["respuestas"].apply(len).max()):
            df[f"respuesta_{i+1}_programa"] = None
            df[f"respuesta_{i+1}_total"] = None

        for i, row in df.iterrows():
            respuestas = row["respuestas"]
            if respuestas:
                for j, respuesta in enumerate(respuestas):
                    df.at[i, f"respuesta_{j+1}_programa"] = respuesta.get("name")
                    df.at[i, f"respuesta_{j+1}_total"] = respuesta.get("total")

        df = df.drop(columns=["respuestas"])
        excel_buffer = io.BytesIO()

        writter = pd.ExcelWriter(excel_buffer, engine="xlsxwriter")
        df.to_excel(writter, sheet_name="Hoja1", index=False)

        writter.close()
        excel_buffer.seek(0)
        archivo = excel_buffer.getvalue()
        response = HttpResponse(
            archivo,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = "attachment; filename=report.xlsx"
        return response

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get("filter") == "facultad":
                f2 = kwargs.get("facultad", None)
                generar = kwargs.get("generar", None)
                if f2 and not generar:
                    response_info = self.get_programa_facultad(int(f2))
                    return Response(response_info)
                elif f2 and generar:
                    response_info = self.get_programa_facultad(int(f2))
                    return self.get_response_excel(response_info)
                response_info = self.get_facultad()
                return Response(response_info)
            else:
                response_info = self.get_programa()
                return Response(response_info)

        except Exception as e:
            return Response({"error": e.args}, status=status.HTTP_404_NOT_FOUND)
