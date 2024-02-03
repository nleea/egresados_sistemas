from rest_framework.views import APIView
from ...serializers.auth.auth_serializers import LoginSerializers, RegisterSerializers
from ...serializers.resources.resources_serializers import ResourcesSerializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth import login
from ....models import Resources


class AuthLogin(APIView):
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def post(self, request, *args, **kwargs):
        data = {}
        if "email" in request.data:
            data["username"] = request.data["email"]
            data["password"] = request.data["password"]
        else:
            data = request.data

        serializers = LoginSerializers(
            data=request.data, context={"request": self.request}
        )
        if not serializers.is_valid():
            return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)

        login(request, serializers.validated_data)  # type: ignore
        token = self.get_tokens_for_user(serializers.validated_data)

        resources = (
            Resources.objects.defer("createdAt", "updateAt")
            .distinct()
            .filter(roles__in=serializers.validated_data.groups.all())
            .order_by("pk")
        )  # type:ignore

        menu = ResourcesSerializers(resources, many=True)

        persons = serializers.validated_data.persons_set.first()  # type: ignore
        request.session["refresh-token"] = token["refresh"]
        return Response(
            {
                "token": token,
                "user": {
                    "name": serializers.validated_data.username,  # type: ignore
                    "id": serializers.validated_data.id,
                    "full_name": f"{persons.name} {persons.surname}",
                },  # type: ignore
                "menu": menu.data,
            },
            status.HTTP_200_OK,
        )


class AuthRegister(APIView):
    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):
        registerUser = RegisterSerializers(data=request.data)
        if registerUser.is_valid():
            password = make_password(
                registerUser.validated_data["password"]
            )  # type:ignore
            registerUser.save(password=password, persona=request.data["persona"])
            return Response("Registro Exitosos", status.HTTP_200_OK)
        return Response(registerUser.errors, status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            jwt_token = request.session.get("refresh-token", None)
            resp = HttpResponse("content")
            resp.cookies.clear()
            resp.flush()
            token = RefreshToken(jwt_token)
            token.blacklist()
            logout(request)
            request.session.clear()
            resp.flush()
            request.session.flush()
            return Response("Ok", status.HTTP_200_OK)
        except TokenError as TkError:
            return Response(f"{TkError}", status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status.HTTP_400_BAD_REQUEST)
