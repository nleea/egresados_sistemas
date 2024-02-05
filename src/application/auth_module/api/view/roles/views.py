from rest_framework.response import Response
from src.application.auth_module.api.serializers.roles.roles_serializers import (
    RolesSerializers,
    RolesSerializersCreate,
)
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.auth_interactor import AuthViewSetFactory
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class RoleViewSet(ViewSet):
    viewset_factory: AuthViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action in ["post"]:
            return RolesSerializersCreate
        return RolesSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def get(self, request, *args, **kwargs):
        payload, status = self.controller.get_all()
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
            payload, status = self.controller.delete_roles(
                None, request.data.get("ids", None)
            )
            return Response(data=payload, status=status)

        payload, status = self.controller.delete_roles(int(instance_id), request.data)
        return Response(data=payload, status=status)

    def get_roles(self, request, *args, **kwargs):
        pk = kwargs.get("id", None)

        if pk == None:
            return Response("Group is required", status=400)

        payload, status = self.controller.get_roles(pk)
        return Response(payload, status=status)

