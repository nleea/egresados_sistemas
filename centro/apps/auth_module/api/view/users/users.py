from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import status
from ...serializers.user.users_serializers import UserSerializers, CreateUserSerializers, UserChangePassword
from ....models import User
from ..modules import create_response


class UsersView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        try:
            request_user = self.request.user.id
            user = User.objects.get(pk=request_user)
            return user
        except User.DoesNotExist:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found')
            return Response(response, status=code)
        except Exception as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, e)
            return Response(response, status=code)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            users = self.get_queryset()
            serializers = UserSerializers(
                users, context={'request': request}, many=True)
            response, code = create_response(
                status.HTTP_200_OK, serializers.data)
            return Response(response, status=code)
        data = self.get_object()
        serializers = UserSerializers(data)
        response, code = create_response(
            status.HTTP_200_OK, serializers.data)
        return Response(response, status=code)


class UsersViewPublic(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializers = UserSerializers(users, many=True)
        response, code = create_response(
            status.HTTP_200_OK, serializers.data)
        return Response(response, status=code)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializers

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def post(self, request, *args, **kwargs):
        userSerializers = self.get_serializer(data=request.data)
        if userSerializers.is_valid():
            self.perform_create(userSerializers)
            response, code = create_response(
                status.HTTP_200_OK, userSerializers.data)
            return Response(userSerializers.data, status=code)
        response, code = create_response(
            status.HTTP_200_OK, userSerializers.data)
        return Response(response, status=code)


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        try:
            request_user = self.kwargs['pk']
            user = User.objects.get(pk=request_user)
            return user
        except User.DoesNotExist:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found')
            raise Response(response, status=code)
        except Exception as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, e)
            return Response(response, status=code)

    def perform_update(self, serializer):
        if 'original-password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()
        if 'original-password' not in self.request.data:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password not found')
            return Response(response, status=code)

        if not user.check_password(request.data['original-password']):
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password is not correct.')
            return Response(response, status=code)

        userSerializers = UserChangePassword(
            user, data=request.data, partial=partial)

        if userSerializers.is_valid():
            self.perform_update(userSerializers)
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password is not correct.')
            return Response(response, status=code)
        return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()

        userSerializers = UserSerializers(
            user, data=request.data, partial=partial)
        if userSerializers.is_valid():
            self.perform_update(userSerializers)
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password is not correct.')
            return Response(response, status=code)
        return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
