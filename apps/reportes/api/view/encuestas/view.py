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
    AswerSerialzersViewa,
    ReporteSerializersViewa,
    QuestionSerializersViewda,
)

import numpy as np
import pandas as pd


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
            return 0, 0

        faculty_percentage = (total_answer_users / count) * 100
        return faculty_percentage, total_answer_users

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
                porcentaje, count_facultad = self.get_faculty_percentage(
                    answer, faculty["id"], count
                )
                answer_data["facultades"].append(
                    {
                        "name": faculty["name"],
                        "porcentaje": porcentaje,
                        "count": count_facultad,
                    }
                )

            response_data["respuestas"].append(answer_data)

        return response_data

    def get(self, request, *args, **kwargs):
        data = self.get_question_with_answers(1)

        return Response(data, status=status.HTTP_200_OK)


class ReportesUser(APIView):
    def get_faculty_percentage(self, answer, count):
        total_answer_users = (
            AnswerUser.objects.filter(
                respuesta=answer,
                pregunta=answer.pregunta,
            )
            .defer("userCreate", "userUpdate", "user__persons__program__faculty")
            .select_related(
                "respuesta",
                "pregunta",
                "user",
            )
            .count()
        )

        if total_answer_users == 0:
            return 0, 0

        faculty_percentage = (total_answer_users / count) * 100
        return faculty_percentage, total_answer_users

    def get_question_with_answers(self, question_id):
        question = Question.objects.get(id=question_id)
        answers = (
            Answer.objects.filter(pregunta__pk=question.pk)
            .defer("userCreate", "userUpdate")
            .select_related("pregunta")
        )

        response_data = {"pregunta": question.pregunta_nombre, "respuestas": []}

        for answer in answers:
            answer_data = {"respuesta": answer.respuesta, "porcentaje": 0, "count": 0}
            count = (
                AnswerUser.objects.filter(pregunta=answer.pregunta)
                .defer("userCreate", "userUpdate", "user")
                .select_related("respuesta", "pregunta")
                .count()
            )
            porcentaje, count_facultad = self.get_faculty_percentage(answer, count)
            answer_data["porcentaje"] = porcentaje
            answer_data["count"] = count_facultad

            response_data["respuestas"].append(answer_data)

        return response_data

    def get(self, request, *args, **kwargs):
        
        
        # results_dict = self.get_question_with_answers(1)
        a = QuestionSerializersViewda(Question.objects.all(), many=True).data
        b = AswerSerialzersViewa(Answer.objects.all(), many=True).data
        c = ReporteSerializersViewa(AnswerUser.objects.all(), many=True).data

        question_df = pd.DataFrame(a)
        answer_df = pd.DataFrame(b)
        answer_user_df = pd.DataFrame(c)

        # Merge DataFrames to create a comprehensive dataset
        merged_df = answer_user_df.merge(
            answer_df, left_on="respuesta_id", right_on="id", how="left"
        )
        merged_df = merged_df.merge(
            question_df, left_on="pregunta_id_x", right_on="id", how="left"
        )

        # Calculate the total number of users who answered each question
        total_users_per_question = (
            merged_df.groupby("pregunta_nombre")["user_id"].nunique().reset_index()
        )
        total_users_per_question.rename(
            columns={"user_id": "Total Users"}, inplace=True
        )

        # Calculate the count of each answer for each question
        answer_counts = (
            merged_df.groupby(["pregunta_nombre", "respuesta"])["id_x"]
            .count()
            .reset_index()
        )
        answer_counts.rename(columns={"id_x": "Answer Count"}, inplace=True)

        # Create a dictionary to store the results
        results_dict = []

        # Iterate through questions and organize the data
        for question_name, group in answer_counts.groupby("pregunta_nombre"):
            question_result = {
                "pregunta": question_name,
                "Total Users": total_users_per_question.loc[
                    total_users_per_question["pregunta_nombre"] == question_name,
                    "Total Users",
                ].values[0],
                "Answers": group[["respuesta", "Answer Count"]]
                .set_index("respuesta")
                .to_dict()["Answer Count"],
            }
            # Calculate and add percentages for each answer
            total_users = question_result["Total Users"]
            answers = question_result["Answers"]
            percentages = {
                answer: (count / total_users) * 100 for answer, count in answers.items()
            }

            question_result["Percentages"] = percentages
            results_dict.append(question_result)

        # Print the result as a dictionary

        return Response(results_dict, status=status.HTTP_200_OK)
