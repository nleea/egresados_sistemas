from ..modules import Response
from rest_framework.viewsets import GenericViewSet
from ....models import Document_types
from ...serializers.document.document_serializers import (
    DocumentSerializers,
    DocumentSerializersView,
)
from typing import Optional
from rest_framework.request import Request
from rest_framework.response import Response

from apps.factory.base_interactor import BaseViewSetFactory


class MessageViewSet(GenericViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []

    serializer_class = DocumentSerializers

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DocumentSerializersView
        return DocumentSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(Document_types, self.serializer_class)

    def get(self, request: Request, *args, **kwargs):
        payload, status = self.controller.get()
        return Response(data=payload, status=status)

    def post(self, request: Request, *args, **kwargs):
        payload, status = self.controller.post(request.data)
        return Response(data=payload, status=status)

    def put(self, request: Request, *args, **kwargs):
        message_id = kwargs.get("id", "")
        payload, status = self.controller.put(int(message_id), request.data)
        return Response(data=payload, status=status)

    def delete(self, request, *args, **kwargs):
        document_id = kwargs.get("id", "")

        if "ids" in request.data:
            payload, status = self.controller.delete(
                None, request.data.get("ids", None)
            )
            return Response(data=payload, status=status)

        payload, status = self.controller.delete(int(document_id), request.data)
        return Response(data=payload, status=status)
