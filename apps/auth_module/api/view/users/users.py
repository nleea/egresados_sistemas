from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import status
from ...serializers.user.users_serializers import UserSerializers, CreateUserSerializers, UserChangePassword
from ....models import User


class UsersView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        try:
            request_user = self.request.user.id # type: ignore
            user = User.objects.get(pk=request_user)
            return user
        except User.DoesNotExist:
            return None
        except Exception as e:
            return None

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            users = self.get_queryset()
            serializers = UserSerializers(
                users, context={'request': request}, many=True)
            return Response(serializers.data, status.HTTP_200_OK)

        data = self.get_object()

        if data is None:
            return Response('User Not found',  status.HTTP_400_BAD_REQUEST)

        try:
            serializers = UserSerializers(data)
            return Response(serializers.data, status.HTTP_200_OK)
        except (AttributeError, Exception) as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UsersViewPublic(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializers = UserSerializers(users, many=True)
        return Response(serializers.data, status.HTTP_200_OK)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializers

    def perform_create(self, serializer):
        password = make_password(self.request.data['password']) # type: ignore
        serializer.save(password=password)

    def post(self, request, *args, **kwargs):
        userSerializers = self.get_serializer(data=request.data)
        if userSerializers.is_valid():
            self.perform_create(userSerializers)
            return Response(userSerializers.data, status.HTTP_200_OK)
        return Response(userSerializers.dat, status.HTTP_200_OK)


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        try:
            request_user = self.kwargs['pk']
            user = User.objects.get(pk=request_user)
            return user
        except User.DoesNotExist:
            return None
        except Exception as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()

        if user is None:
            return Response('Password Error', status.HTTP_400_BAD_REQUEST)

        try:
            userSerializers = UserSerializers(
                user, data=request.data, partial=partial)
            if userSerializers.is_valid():
                self.perform_update(userSerializers)
                return Response('Password Error', status.HTTP_400_BAD_REQUEST)
            return Response(userSerializers.errors, 'Error', status=status.HTTP_400_BAD_REQUEST) # type: ignore
        except (AttributeError, Exception) as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class UserChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        try:
            request_user = self.kwargs['pk']
            user = User.objects.get(pk=request_user)
            return user
        except (User.DoesNotExist, TypeError):
            return None
        except (BaseException, TypeError) as e:
            return None

    def perform_update(self, serializer):
        if 'original-password' in self.request.data: # type: ignore
            password = make_password(self.request.data['password']) # type: ignore
            serializer.save(password=password)
        else:
            serializer.save()

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()

        if user is None:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)# type: ignore

        if 'original-password' not in self.request.data: # type: ignore
            return Response('Password Error', status.HTTP_400_BAD_REQUEST)

        if not user.check_password(request.data['original-password']):
            return Response('Password is not correct.', status.HTTP_400_BAD_REQUEST)

        userSerializers = UserChangePassword(
            user, data=request.data, partial=partial, context={'context': request})

        try:
            if userSerializers.is_valid():
                self.perform_update(userSerializers)
                return Response('Password Change', status.HTTP_200_OK)
            return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)
