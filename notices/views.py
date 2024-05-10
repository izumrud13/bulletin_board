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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NoticesFilter


class NoticesCreateApiView(generics.CreateAPIView):
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для автоматческой привязки объявления к пользователю"""
        serializer.save(author=self.request.user)


class NoticesUpdateApiView(generics.UpdateAPIView):
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class NoticesRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated]


class NoticesDestroyApiView(generics.DestroyAPIView):
    serializer_class = NoticesDetailSerializers
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
