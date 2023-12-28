from ...serializers.advertissement.advertisement_serialziers import (
    AdvertisementSerializers,
    AdvertisementSerializersView,
    AdvertisementVotoSerializers,
    AdvertisementsMensajes,
)
from ....models.models import (
    RedesSociales,
    TiposCapacitaciones,
    Mensajes,
)
from rest_framework.response import Response
from django.db import models
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.classified_interactor import BaseViewSetFactory


class AdvertisementViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        print(self.action)

        if self.action in ["get", "mine", "most_view", "query"]:
            return AdvertisementSerializersView
        elif self.action == "save_voto":
            return AdvertisementVotoSerializers
        elif self.action == "state_changes":
            return AdvertisementsMensajes
        return AdvertisementSerializers

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

    def mine(self, request, *args, **kwargs):
        payload, status = self.controller.complex_filters(
            defer=[
                "tipo_capacitacion__userCreate_id",
                "redes__userUpdate_id",
                "redes__userCreate_id",
                "subCategoria__userCreate_id",
                "userCreate",
                "userUpdate",
            ],
            related=["subCategoria", "subCategoria__categoriaId"],
            prefetch=["redes", "tipo_capacitacion", "mensajes"],
            filter=[{"visible": True, "userCreate": request.user.id}],
            order=["-id"],
        )

        return Response(data=payload, status=status)

    def save_voto(self, request, *args, **kwargs):
        emprendimiento: int = request.data.get("emprendimiento")
        payload, status = self.controller.save_voto(
            data={"emprendimiento": emprendimiento, "user": request.user.id}
        )
        return Response(data=payload, status=status)

    def most_view(self, request, *args, **kwargs):
        payload, status = self.controller.complex_filters(
            defer=[
                "tipo_capacitacion__userCreate_id",
                "redes__userUpdate_id",
                "redes__userCreate_id",
                "subCategoria__userCreate_id",
            ],
            related=[
                "subCategoria",
                "userCreate",
                "userUpdate",
                "subCategoria__categoriaId",
            ],
            prefetch=["redes", "tipo_capacitacion"],
            annotate=[{"nun_votos": models.Count("votoanuncio")}],
            order=["-nun_votos"],
            filter=[{"visible": True, "state": True}],
        )

        return Response(data=payload[:10], status=status)

    def state_changes(self, request, *args, **kwargs):
        state = request.data.get("state", False)
        mensajes = request.data.get("mensaje", None)

        pk = kwargs.get("id")
        i, s = self.controller.state_changes(
            id=pk, data={"mensajes": mensajes, "state": state}
        )

        return Response(i, status=s)

    def get(self, request, *args, **kwargs):
        sub_category = request.GET.get("subCategoryId", None)

        if sub_category:
            payload, status = self.controller.anuncio_subCategory(
                sub_category=sub_category, user_id=request.user.id
            )

            return Response(data=payload, status=status)

        payload, status = self.controller.complex_filters(
            defer=[
                "tipo_capacitacion__userCreate_id",
                "redes__userUpdate_id",
                "redes__userCreate_id",
                "subCategoria__userCreate_id",
                "subCategoria__userUpdate_id",
                "userCreate",
                "userUpdate",
                "subCategoria__categoriaId__userUpdate_id",
                "subCategoria__categoriaId__userCreate_id",
                "mensajes__userCreate_id",
                "mensajes__userUpdate_id",
            ],
            related=["subCategoria", "subCategoria__categoriaId"],
            prefetch=[
                models.Prefetch(
                    "redes", RedesSociales.objects.all().only("id", "name", "link")
                ),
                models.Prefetch(
                    "tipo_capacitacion",
                    TiposCapacitaciones.objects.all().only("id", "name"),
                ),
                models.Prefetch(
                    "mensajes",
                    Mensajes.objects.all().only(
                        "id", "mensaje", "createdAt", "updateAt"
                    ),
                ),
            ],
            filter=[{"visible": True}],
            order=["-id"],
        )
        return Response(data=payload, status=status)

    def query(self, request, *args, **kwargs):
        if "categoryId" in request.data:
            payload, status = self.controller.query(
                sub_category=request.data.get("categoryId"),
                user_id=request.user.id,
                excludes=["mensajes"],
            )
            return Response(data=payload, status=status)
        return Response("NOT_FOUND", status=404)
