from apps.pqrs.api.serializers.respuesta.respuesta_serializers import (
    RespuestaSerializers,
    RespuestaSerializersView,
)
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from typing import Optional
from apps.factory.pqrs_interactor import BaseViewSetFactory


class RespuestaViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action in ["get", "query"]:
            return RespuestaSerializersView
        return RespuestaSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def post(self, request, *args, **kwargs):
        payload, status = self.controller.post_respuesta(
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
            related=["pqrs", "pqrs__tipopqrs", "pqrs__persona"],
            order=["-id"],
        )

        return Response(data=payload, status=status)

    def query(self, request, *args, **kwargs):
        pqrs_id = request.data["pqrs"]

        payload, status = self.controller.query(pqrs_id)

        return Response(payload, status)
