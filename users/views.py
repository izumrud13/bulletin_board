from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializers, UserRegisterSerializer


# Create your views here.
class UserListApiView(generics.ListAPIView):
    """Класс для просмотра списка пользователей"""
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateApiView(generics.CreateAPIView):
    """Класс для регистрации пользователя"""
    serializer_class = UserRegisterSerializer

    def create(self, request):
        """Метод для хэширования пароля пользователя в БД"""
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserUpdateApiView(generics.UpdateAPIView):
    """Класс для обновления данных пользователя, добавить Owner"""
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveApiView(generics.RetrieveAPIView):
    """Класс для просмотра пользователя"""
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
