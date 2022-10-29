from rest_framework.views import APIView
from ...serializers.auth.auth_serializers import LoginSerializers, RegisterSerializers
from ...serializers.resources.resources_serializers import ResourcesSerializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from ..modules import create_response
from rest_framework import status
from ....models import Resources_roles, Resources


class AuthLogin(APIView):
    serializer_class = LoginSerializers

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self, request, *args, **kwargs):
        data = {}
        if 'email' in request.data:
            data['username'] = request.data['email']
            data['password'] = request.data['password']
        else:
            data = request.data
        serializers = LoginSerializers(
            data=data, context={'request': self.request})
        if not serializers.is_valid():
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, serializers.errors)
            return Response(response, status=code)

        token = self.get_tokens_for_user(serializers.validated_data)

        resourcesRoles = Resources_roles.objects.filter(
            rolesId__in=[x for x in serializers.validated_data.roles.all()])
        resources = Resources.objects.filter(
            id__in=[x.resourcesId.pk for x in resourcesRoles])

        menu = ResourcesSerializers(resources, many=True)
        request.session['refresh-token'] = token['refresh']
        response, code = create_response(
            status.HTTP_200_OK, {'token': token, 'user': {'name': serializers.validated_data.username, 'id': serializers.validated_data.id}, 'menu': menu.data})
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


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            jwt_token = request.session.get('refresh-token', None)
            token = RefreshToken(jwt_token)
            token.blacklist()
            logout(request)
            request.session.flush()
            response, code = create_response(
                status.HTTP_200_OK, 'Ok')
            return Response(response, code)
        except TokenError as TkError:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, f'{TkError}')
            return Response(response, code)
        except Exception as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, e)
            return Response(response, code)
