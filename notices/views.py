from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from notices.filters import NoticesFilter
from notices.models import Notice
from notices.paginators import CustomPagination
from notices.permissions import IsOwner, IsAdmin
from notices.serializers import NoticesSerializers, NoticesDetailSerializers


# Create your views here.
class NoticesListApiView(generics.ListAPIView):
    """Просмотр всех объявлений"""
    serializer_class = NoticesSerializers
    queryset = Notice.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,) # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = NoticesFilter # Выбираем созданный фильтр


class NoticesCreateApiView(generics.CreateAPIView):
    """Создание объявления"""
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для автоматческой привязки объявления к пользователю"""
        serializer.save(author=self.request.user)


class NoticesUpdateApiView(generics.UpdateAPIView):
    """Редактирование объявления"""
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class NoticesRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр объявления"""
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated]


class NoticesDestroyApiView(generics.DestroyAPIView):
    """Удаление объявлений"""
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class UserNoticesListApiView(generics.ListAPIView):
    """Просмотр объявлний текущего пользовтаеля"""
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Notice.objects.filter(author=self.request.user)
