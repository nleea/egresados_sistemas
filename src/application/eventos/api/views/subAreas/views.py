from src.application.eventos.api.serializers.eventos.eventos_sub_area_serializers import (
    EventosSubAreaSerializers,
    EventosSubAreaSerializersView,
)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.eventos_interactor import BaseViewSetFactory


class SubAreaViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action in ["get", "query"]:
            return EventosSubAreaSerializersView
        return EventosSubAreaSerializers

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
        payload, status = self.controller.complex_filters(
            filter=[{"visible": True}],
            related=["area"],
            defer=[
                "userCreate",
                "userUpdate",
                "area__userCreate_id",
                "area__userUpdate_id",
            ],
            order=["-id"],
        )

        return Response(data=payload, status=status)

    def query(self, request, *args, **kwargs):
        area = request.data.get("area", None)

        payload, status = self.controller.query(area=area)

        return Response(data=payload, status=status)
