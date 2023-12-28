from src.application.encuestas.api.serializers.questions.questions_serializers import (
    QuestionSerializers,
    QuestionSerializersView,
    QuestionCreateSerializers,
)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.encuestas_interactor import BaseViewSetFactory


class QuestionsViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action == "get":
            return QuestionSerializersView
        elif self.action == "post":
            return QuestionCreateSerializers
        return QuestionSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def post(self, request, *args, **kwargs):
        payload, status = self.controller.post(
            request.data, extra={"userCreate": request.user}
        )
        return Response(data=payload, status=status)

    def put(self, request, *args, **kwargs):
        instance_id = kwargs.get("id", "")
        payload, status = self.controller.put(int(instance_id), request.data)
        return Response(data=payload, status=status)

    def delete(self, request, *args, **kwargs):
        instance_id = kwargs.get("id", "")

        if "ids" in request.data:
            payload, status = self.controller.delete(
                None, request.data.get("ids", None)
            )
            return Response(data=payload, status=status)

        payload, status = self.controller.delete(int(instance_id), request.data)
        return Response(data=payload, status=status)

    def get(self, request, *args, **kwargs):
        payload, status = self.controller.get_filter_related(
            filter_param=[{"visible": True}],
            related=["depende_respuesta", "depende_respuesta__pregunta", "momento"],
            prefetch=["answer_set"],
            order=["-id"],
        )

        return Response(data=payload, status=status)

    def question_response(self, request, *args, **kwargs):
        payload, status = self.controller.question_response(request.data, request.user)
        return Response(payload, status)
