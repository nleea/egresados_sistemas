from apps.interfaces.controllers.base_controller import BaseController
from rest_framework import status
from apps.encuestas.models import AnswerUser


class EncuestasController(BaseController):
    def __init__(self, repo, serializer) -> None:
        super().__init__(repo, serializer)

    def question_response(self, data, user):
        try:
            aswer_create = []
            for i in data["respuestas"]:
                if i["type"] == "unica respuesta":
                    aswer_create.append(
                        AnswerUser(
                            pregunta_id=i["pregunta"],
                            respuesta_id=i["respuesta"],
                            user=user,
                        )
                    )
                elif i["type"] == "pregunta corta" or i["type"] == "pregunta larga":
                    aswer_create.append(
                        AnswerUser(
                            pregunta_id=i["pregunta"],
                            texto=i["respuesta"],
                            user=user,
                        )
                    )
                elif i["type"] == "multiple":
                    for x in i["respuesta"]:
                        aswer_create.append(
                            AnswerUser(
                                pregunta_id=i["pregunta"],
                                respuesta_id=x,
                                user=user,
                            )
                        )

            AnswerUser.objects.bulk_create(aswer_create)

            return "Exitoso", status.HTTP_200_OK
        except Exception as e:
            return e.args, status.HTTP_400_BAD_REQUEST
