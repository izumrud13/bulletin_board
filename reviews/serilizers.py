from rest_framework import serializers

from reviews.models import Review


class ReviewSerializers(serializers.ModelSerializer):
    """Сериализатор для просмотра отзывов"""
    class Meta:
        model = Review
        fields = '__all__'
