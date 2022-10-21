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
            request_user = self.request.user.id
            user = User.objects.get(pk=request_user)
            return user
        except User.DoesNotExist:
            return Response({'message': 'Not Found'},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': e})

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            users = self.get_queryset()
            serializers = UserSerializers(
                users, context={'request': request}, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        data = self.get_object()
        serializers = UserSerializers(data)
        return Response(serializers.data, status=status.HTTP_200_OK)


class UsersViewPublic(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializers = UserSerializers(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


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
            return Response(userSerializers.data, status=status.HTTP_200_OK)
        return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        try:
            request_user = self.kwargs['pk']
            user = User.objects.get(pk=request_user)
            return user
        except User.DoesNotExist:
            raise Response({'message': 'Not Found'},
                           status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': e})

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
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(request.data['original-password']):
            return Response(
                {'state': False, 'code': 1, 'message': 'Password is not correct.'},
                status=status.HTTP_200_OK)

        userSerializers = UserChangePassword(
            user, data=request.data, partial=partial)

        if userSerializers.is_valid():
            self.perform_update(userSerializers)
            return Response({'message': 'Ok'}, status=status.HTTP_200_OK)
        return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()

        userSerializers = UserSerializers(
            user, data=request.data, partial=partial)
        if userSerializers.is_valid():
            self.perform_update(userSerializers)
            return Response(userSerializers.data, status=status.HTTP_200_OK)
        return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
