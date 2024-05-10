from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Аутентификация автора объявления"""
    message = 'Вы не являетесь автором'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class IsAdmin(BasePermission):
    """Проверка на права администратора"""

    def has_permission(self, request, view):
        if request.user.grups.filter(name='Admin').exists():
            return True
        return False
