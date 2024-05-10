from django.conf import settings
from django.db import models
from django.utils import timezone


from notices.models import Notice

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Review(models.Model):
    """Класс модели отзывов"""
    text = models.CharField(max_length=100, verbose_name='Текст')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Notice, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время')

    def __str__(self):
        return f'{self.text}-{self.author}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
