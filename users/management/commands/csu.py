from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Команда для создания супер-пользователя
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('1234')
        user.save()