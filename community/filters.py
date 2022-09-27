from django_filters import (
    FilterSet,
    CharFilter,
)

from .models import Community


class CommunityFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")
    description = CharFilter(lookup_expr="icontains")
    category = CharFilter(lookup_expr="icontains")
    writer_nickname = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Community
        fields = ['title', 'description', 'category','writer_nickname']

    def __init__(self, *args, **kwargs):
        super(CommunityFilter, self).__init__(*args, **kwargs)
