from django.shortcuts import render
from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializer import *

class ClubsViewSet(ModelViewSet):
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer


class ClubsArticleViewSet(ModelViewSet):
    queryset = Clubboard.objects.all()
    serializer_class = ClubBoardSerializer

    @action(detail=True, methods=['GET'])
    def article_list(self, request, **kwargs):
        article_query = self.queryset.filter(club_id=self.kwargs.get('club_pk', ''))
        serializer = self.get_serializer(article_query, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['POST'])
    def article_create(self, request, **kwargs):
        request.data._mutable = True
        request.data['club_id'] = str(self.kwargs.get('club_pk', ''))
        request.data._mutable = False
        print(request.data)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()        
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

clubs_article_list = ClubsArticleViewSet.as_view({
    'get': 'article_list',
    'post': 'article_create',
})

clubs_article_detail = ClubsArticleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})