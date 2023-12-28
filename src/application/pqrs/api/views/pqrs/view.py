from src.application.pqrs.api.serializers.pqrs.pqrs_serialziers import (
    PqrsSerializers,
    PqrsSerializersView,
)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.pqrs_interactor import BaseViewSetFactory


class PqrsViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action == "get":
            return PqrsSerializersView
        return PqrsSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def post(self, request, *args, **kwargs):
        payload, status = self.controller.post(
            request.data,
            extra={
                "userCreate": request.user,
            },
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
        status_pqrs = request.GET.get("status", "AC")
        order_pqrs = request.GET.get("order", "-id")
        start_pqrs = request.GET.get("startdate", None)
        end_pqrs = request.GET.get("enddate", None)

        payload, status = self.controller.pqrs_filter(
            start=start_pqrs,
            end=end_pqrs,
            user=request.user,
            order=order_pqrs,
            status=status_pqrs,
        )

        return Response(data=payload, status=status)
