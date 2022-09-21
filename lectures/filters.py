from django_filters import (
    FilterSet,
    CharFilter,
)

from .models import Lectures


class LecturesFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")
    description = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Lectures
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(LecturesFilter, self).__init__(*args, **kwargs)
