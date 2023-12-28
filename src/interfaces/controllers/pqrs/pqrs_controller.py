from src.interfaces.controllers.base_controller import BaseController
from src.application.pqrs.api.serializers.pqrs.pqrs_serialziers import (
    PqrsSerializers,
    PqrsSerializersView,
)
from src.application.pqrs.models import Pqrs, Asignacion
from django.db.models import Prefetch
from rest_framework import status


class PqrsController(BaseController):
    def __init__(self, repo, serializer) -> None:
        super().__init__(repo, serializer)

    def post_respuesta(self, data, extra=None):
        resp, status = self.post(data, extra)

        if status == 201 and "status" in data:
            instance = Pqrs.objects.get(pk=data["pqrs"])
            resulst = PqrsSerializers(
                instance, {"status": data["status"]}, partial=True
            )
            if resulst.is_valid():
                resulst.save()

        return resp, status

    def query(self, pk):
        pqrs = (
            Pqrs.objects.defer(
                "userCreate",
                "userUpdate",
                "tipopqrs__userCreate",
                "tipopqrs__userUpdate",
            )
            .prefetch_related(
                Prefetch(
                    "respuesta_pqrs",
                    queryset=self.repo.get_all(related=["userCreate", "userUpdate"]),
                )
            )
            .select_related("tipopqrs", "persona")
            .get(pk=pk)
        )

        respuestas = pqrs._prefetched_objects_cache["respuesta_pqrs"]  # type:ignore

        if pqrs is None:
            return "PQRS with id {} not exist".format(pk), status.HTTP_400_BAD_REQUEST

        resulst = PqrsSerializersView([pqrs], many=True)
        resulst_respuestas = self.serializer(respuestas, many=True)

        response = {"pqrs": resulst.data, "respuestas": resulst_respuestas.data}

        return response, status.HTTP_200_OK

    def pqrs_filter(self, start, end, user, **kwargs):
        order = kwargs.get("order", "-id")
        status_pqrs = kwargs.get("status", "-id")
        prefetch = [
            Prefetch(
                "asignacion_set",
                queryset=Asignacion.objects.all().defer(
                    "userCreate",
                    "userUpdate",
                    "funcionarioId",
                    "fecha_asignacion",
                    "updateAt",
                    "createdAt",
                ),
            )
        ]

        defer = [
            "tipopqrs__userCreate_id",
            "tipopqrs__userUpdate_id",
            "userUpdate",
        ]

        filters = {"visible": True, "status": status_pqrs}

        if start and end:
            resp, status = self.complex_filters(
                defer=defer,
                related=["persona", "tipopqrs", "userCreate"],
                prefetch=prefetch,
                filter=[
                    {"userCreate": user.id, "createdAt__range": [start, end], **filters}
                ],
                order=[order],
            )

            return resp, status

        rol = user.groups.filter(name="Admin")

        if rol:
            resp, status = self.complex_filters(
                defer=[*defer, "userCreate"],
                related=["persona", "tipopqrs"],
                prefetch=prefetch,
                filter=[filters],
                order=[order],
            )
            return resp, status
        else:
            resp, status = self.complex_filters(
                defer=[*defer],
                related=["persona", "tipopqrs"],
                prefetch=prefetch,
                filter=[{**filters, "userCreate": user.id}],
                order=[order],
            )

            return resp, status
