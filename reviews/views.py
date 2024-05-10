from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from notices.models import Notice
from notices.permissions import IsOwner, IsAdmin
from reviews.models import Review
from reviews.serilizers import ReviewSerializers


# Create your views here.

class ReviewListApiView(generics.ListAPIView):
    """Просмотр всех отзывов"""
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [AllowAny]


class ReviewCreateApiView(generics.CreateAPIView):
    """Создание отзыва"""
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для автоматичесой привязки пользователя к отзыву"""
        ad_pk = self.kwargs.get('ad_pk')
        ad_for_comment = Notice.objects.get(pk=ad_pk)
        comment_pk = self.kwargs.get('pk')
        serializer.save(author=self.request.user, ad=ad_for_comment, pk=comment_pk)


class ReviewUpdateApiView(generics.UpdateAPIView):
    """Редактирование отзыва"""
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]

class ReviewDestroyApiView(generics.DestroyAPIView):
    """Удаление отзыва"""
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
