from ...serializers.category.category_serializers import (
    CategorySerializers,
    CategorySerializersView,
)

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from typing import Optional
from apps.factory.base_interactor import BaseViewSetFactory


class CategoryViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action == "get":
            return CategorySerializersView
        return CategorySerializers

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
            filter_param=[{"visible": True}], related=["userCreate", "userUpdate"]
        )

        return Response(data=payload, status=status)
