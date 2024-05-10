from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Notice(models.Model):
    """Класс модели объявления"""
    title = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    descriptions = models.CharField(max_length=500, verbose_name='Описание товара')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='notices/', verbose_name='Изображение товара', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания объявления')

    def __str__(self):
        return f'{self.title}-{self.price}'

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']
