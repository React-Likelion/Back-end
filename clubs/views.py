from django.shortcuts import render
from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializer import *

class ClubsViewSet(ModelViewSet):
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk_2'
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer

    @action(detail=True)
    def articles(self, request, pk):
        board_queryset = Clubboard.objects.filter(clud_id=pk)
        serializer = self.get_serializer(board_queryset, many=True)
        return Response(serializer.data)



class ClubsNewViewSet(ModelViewSet):
    queryset = Clubs.objects.all().order_by('-id')
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