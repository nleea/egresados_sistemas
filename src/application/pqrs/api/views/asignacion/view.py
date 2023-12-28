from src.application.pqrs.api.serializers.asignacion.asignacion_serializers import (
    AsignacionSerializers,
    AsignacionSerializerView,
)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.pqrs_interactor import BaseViewSetFactory


# class AsignacionPqrsView(APIView):
#     def get(self, request, *args, **kwargs):
#         roles = request.user.groups.get(name="Admin")

#         if roles:
#             pqrs_filter = (
#                 Pqrs.objects.select_related("persona", "tipopqrs")
#                 .filter(status="AC", visible=True)
#                 .order_by("-id")
#             )
#             data = PqrsSerializersView(pqrs_filter, many=True, meta=True)
#             return Response(data.data, status.HTTP_200_OK)

# from ...serializers.pqrs.pqrs_serialziers import PqrsSerializersView


class AsignacionViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action == "get":
            return AsignacionSerializerView
        return AsignacionSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def post(self, request, *args, **kwargs):
        payload, status = self.controller.post(
            request.data,
            extra={
                "funcionarioId": request.user.id,
                "pqrs": request.data["pqrs"],
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
        payload, status = self.controller.complex_filters(
            defer=[
                "userCreate",
                "userUpdate",
                "pqrs__userCreate_id",
                "pqrs__userUpdate",
                "pqrs__tipopqrs__userCreate_id",
                "pqrs__tipopqrs__userUpdate_id",
            ],
            filter=[{"funcionarioId": request.user.id, "pqrs__visible": True}],
            related=["pqrs", "pqrs__tipopqrs", "pqrs__persona"],
            order=["-id"],
        )

        return Response(data={"pqrs": [x["pqrs"] for x in payload]}, status=status)
