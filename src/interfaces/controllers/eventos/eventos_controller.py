from src.interfaces.controllers.base_controller import BaseController
from src.application.eventos.models.models import Asistencia
from django.db import models
from django.utils import timezone


class EventosController(BaseController):
    def __init__(self, repo, serializer) -> None:
        super().__init__(repo, serializer)

    def get_eventos(self, admin, user, **kwargs):
        order_evento = kwargs.get("order", "-id")
        start = kwargs.get("start", None)
        end = kwargs.get("end", None)

        defer = [
            "userCreate",
            "userUpdate",
            "area__userCreate",
            "area__userUpdate",
            "subArea__userCreate",
            "subArea__userUpdate",
            "tipo__userCreate",
            "tipo__userUpdate",
        ]
        filters = {"visible": True}
        related = ["area", "subArea", "tipo"]

        annotate = [
            {
                "confirm_asistencia": models.Exists(
                    Asistencia.objects.filter(
                        evento=models.OuterRef("pk"), user=user.id, confirm=True
                    )
                ),
                "fecha_pasada": models.Case(
                    models.When(fecha__lt=timezone.now().date(), then=True),
                    default=False,
                    output_field=models.BooleanField(),
                ),
            }
        ]

        if admin:
            return self.complex_filters(
                defer=defer,
                related=related,
                filter=filters,
                order=[order_evento],
                annotate=annotate,
            )
        else:
            if start and end:
                return self.complex_filters(
                    defer=defer,
                    related=related,
                    filter={
                        **filters,
                        "inscripcion__user": user.id,
                        "fecha__range": [start, end],
                    },
                    order=[order_evento],
                    annotate=annotate,
                )
            else:
                return self.complex_filters(
                    defer=defer,
                    related=related,
                    filter={
                        **filters,
                        "inscripcion__user": user.id,
                    },
                    order=[order_evento],
                    annotate=annotate,
                )

    def query(self, area):
        return self.complex_filters(
            defer=[
                "userCreate",
                "userUpdate",
                "area__userCreate_id",
                "area__userUpdate_id",
            ],
            related=["area"],
            filter={"area": area},
            order=["-id"],
        )
