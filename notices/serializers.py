from rest_framework import serializers

from notices.models import Notice


class NoticesSerializers(serializers.ModelSerializer):
    """Сериализатор для просмотра объявлений"""

    class Meta:
        model = Notice
        fields = ['title', 'price', 'descriptions', 'image']
