from rest_framework import serializers

from notices.models import Notice


class NoticesSerializers(serializers.ModelSerializer):
    """Сериализатор для просмотра объявлений"""

    class Meta:
        model = Notice
        fields = ['title', 'price', 'descriptions', 'image']


class NoticesDetailSerializers(serializers.ModelSerializer):
    """Сериалайзер для просмотра одного объявления"""

    class Meta:
        model = Notice
        fields = '__all__'
