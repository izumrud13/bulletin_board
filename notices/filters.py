import django_filters

from notices.models import Notice


class NoticesFilter(django_filters.rest_framework.FilterSet):
    """Фильтрация объявлений"""
    # CharFilter — специальный фильтр, который позволяет искать совпадения в текстовых полях модели
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', )

    class Meta:
        model = Notice
        fields = ('title',)
