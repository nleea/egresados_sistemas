from rest_framework.views import APIView
from ...serializers.auth.auth_serializers import LoginSerializers, RegisterSerializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from ..modules import create_response
from rest_framework import status


class AuthLogin(APIView):
    serializer_class = LoginSerializers

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self, request, *args, **kwargs):
        serializers = LoginSerializers(data=request.data)
        if not serializers.is_valid():
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, serializers.errors)
            return Response(response, status=code)

        token = self.get_tokens_for_user(serializers.validated_data)
        response, code = create_response(
            status.HTTP_200_OK, {'token': token, 'user': {'email': serializers.validated_data.email, 'id': serializers.validated_data.id}})
        return Response(response, status=code)


class AuthRegister(APIView):
    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):
        registerUser = RegisterSerializers(data=request.data)
        if registerUser.is_valid():
            password = make_password(
                registerUser.validated_data['password'])
            registerUser.save(password=password)
            response, code = create_response(
                status.HTTP_200_OK, registerUser.data)
            return Response(response, status=code)

        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, registerUser.errors)
        return Response(response, status=code)
