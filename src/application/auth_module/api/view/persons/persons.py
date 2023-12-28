from ..modules import Response
from ...serializers.person.persons_serializers import (
    PersonsSerializers,
    PersonsSimpleSerializersView,
)
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.base_interactor import BaseViewSetFactory


class PersonViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    serializer_class = PersonsSerializers

    def get_serializer_class(self):
        if self.action in ["get"]:
            return PersonsSimpleSerializersView
        return PersonsSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def get(self, request, *args, **kwargs):
        payload, status = self.controller.get_filter_related(
            None, ["document_type", "gender_type"]
        )
        return Response(data=payload, status=status)

    def post(self, request, *args, **kwargs):
        payload, status = self.controller.post(request.data)
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
