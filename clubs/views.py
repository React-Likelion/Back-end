from django.shortcuts import render
from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import *
from .serializer import *

class ClubsViewSet(ModelViewSet):
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer 


class ClubsNewViewSet(ModelViewSet):
    queryset = Clubs.objects.all('-id')
    serializer_class = ClubsSerializer


class ClubsMemberViewSet(ModelViewSet):
    queryset = Clubs.objects.all()\
                .annotate(member_cnt=Count('member'))\
                .order_by('-member_cnt')
    serializer_class = ClubsSerializer
                

clubs_list = ClubsViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

clubs_new_list = ClubsNewViewSet.as_view({
    'get': 'list',
})

clubs_member_list = ClubsMemberViewSet.as_view({
    'get': 'list',
})

clubs_detail = ClubsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})