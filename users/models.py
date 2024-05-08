from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Класс для создания модели пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='Телефон', **NULLABLE)
    image = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
