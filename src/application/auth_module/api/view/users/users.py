from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework import status
from ...serializers.user.users_serializers import (
    UserSerializers,
    CreateUserSerializers,
    UserChangePassword,
)
from ....models import User
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from typing import Optional
from src.factory.base_interactor import BaseViewSetFactory


class UserViewSet(ViewSet):
    viewset_factory: BaseViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action in ["get"]:
            return UserSerializers
        return CreateUserSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def get(self, request, *args, **kwargs):
        all_user = request.GET.get("all", None)

        if request.user.is_staff and all_user:
            payload, status = self.controller.get_filter_related(prefetch=["groups"])
            return Response(data=payload, status=status)

        payload, status = self.controller.get_object(
            request.user.id, prefetch=["groups"]
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


class UserChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        try:
            request_user = self.kwargs["pk"]
            user = User.objects.get(pk=request_user)
            return user
        except (User.DoesNotExist, TypeError):
            return None
        except (BaseException, TypeError) as e:
            return None

    def perform_update(self, serializer):
        if "original-password" in self.request.data:  # type: ignore
            password = make_password(self.request.data["password"])  # type: ignore
            serializer.save(password=password)
        else:
            serializer.save()

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        user = request.user

        if user is None:
            return Response("User don't exist", status.HTTP_400_BAD_REQUEST)  # type: ignore

        if "original-password" not in self.request.data:  # type: ignore
            return Response("Password Error", status.HTTP_400_BAD_REQUEST)

        if not user.check_password(request.data["original-password"]):
            return Response("Password is not correct.", status.HTTP_400_BAD_REQUEST)

        userSerializers = UserChangePassword(
            user, data=request.data, partial=partial, context={"context": request}
        )

        try:
            if userSerializers.is_valid():
                self.perform_update(userSerializers)
                return Response("Password Change", status.HTTP_200_OK)
            return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)
