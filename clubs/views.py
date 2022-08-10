import re
from django.shortcuts import render
from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from accounts.models import Members
from .models import *
from .serializer import *


def include_filter(request, include_field, related_field, queryset):
    filter_list = {}
    
    for i in include_field:
        filter = request.query_params.get(i, None)
        if filter is None: continue
        
        filter_list[f"{i}__regex"] = rf".*{filter}.*"
    
    for i in related_field:
        filter = request.query_params.get(i, None)
        if filter is None: continue
        
        filter_list[i] = filter
    
    return queryset.filter(**filter_list)

class ClubsViewSet(ModelViewSet):
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'field', 'location', 'age_group']
    
    @action(detail=True, method=['POST'])
    def club_signin(self, request, **kwargs):
        club = self.queryset.filter(id=self.kwargs.get('pk'))[0]
        
        sign_id = request.query_params.get('id', None)
        member_list = club.member.all()

        if sign_id is None or Members.objects.get(id=sign_id) in member_list:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if club.member_cnt() >= club.limit:
            content = {'error': 'club is already full!'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        club.member.add(request.query_params.get('id'))
        club.save()

        content = {'ok': 'singin complete!'}
        return Response(content, status=status.HTTP_200_OK)


class ClubsArticleViewSet(ModelViewSet):
    queryset = Clubboard.objects.all()
    serializer_class = ClubBoardSerializer
        
    @action(detail=True, methods=['GET'])
    def article_list(self, request, **kwargs):
        article_query = self.queryset.filter(club_id=self.kwargs.get('club_pk', ''))
        search_field = ['title', 'description', 'category']
        related_field = ['writer_id']

        if request.query_params:
            article_query = include_filter(request, search_field, related_field, article_query)

        serializer = self.get_serializer(article_query, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['POST'])
    def article_create(self, request, **kwargs):
        request.data._mutable = True
        request.data['club_id'] = str(self.kwargs.get('club_pk', ''))
        request.data._mutable = False

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()        
        return Response(serializer.data)


class GalleriesViewSet(ModelViewSet):
    queryset = Galleries.objects.all()
    serializer_class = GalleriesSerializer

    @action(detail=True, methods=['GET'])
    def gallery_list(self, request, **kwargs):
        article_query = self.queryset.filter(club_id=self.kwargs.get('club_pk', ''))
        search_field = ['title', 'description', 'category']
        realted_field = ['writer_id']
        
        if request.query_params:
            article_query = include_filter(request, search_field, realted_field, article_query)
        
        serializer = self.get_serializer(article_query, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['POST'])
    def gallery_create(self, request, **kwargs):
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

    'post': 'club_signin'
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

clubs_galleries_list = GalleriesViewSet.as_view({
    'get': 'gallery_list',
    'post': 'gallery_create',
})

clubs_galleries_detail = GalleriesViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})