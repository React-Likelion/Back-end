from mentorings import models, serializers
from accounts.models import User
from mentorings.models import mentorings, mentoring_chats
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Count

#멘토링 CRUD
class MentoringViewSet(viewsets.ModelViewSet):
    queryset=mentorings.objects.all().order_by('-create_date')
    serializer_class=serializers.MentoringSerializers
    # permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['title', 'age_group', 'location', 'field']

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        serializer.save(member_cnt=1)
        serializer.save(nickname=self.request.user.nickname)

#멘토링 챗 CRUD    
class Mentoring_ChatsViewSet(viewsets.ModelViewSet):
    queryset=mentoring_chats.objects.all().order_by('create_date')
    serializer_class=serializers.Mentoring_chatsSerializers 
    permission_classes=[IsAuthenticated]
            
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)    
        serializer.save(nickname=self.request.user.nickname)
    
    #list요청 오버라이딩
    def list(self, request, pk, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        mentoring=get_object_or_404(mentorings,id=pk)
        member=get_object_or_404(User, nickname=request.user)
        #manytomany테이블에 추가
        mentoring.User.add(member)
        #인원수 증가
        mentoring_member=mentorings.objects.annotate(count=Count('User'))
        mentoring.member_cnt=mentoring_member[pk-1].count
        mentoring.save()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


#foreign-key검색 여부확인 용 임시 viewset
class Locations_ViewSet(viewsets.ModelViewSet):
    queryset=models.locations.objects.all()
    serializer_class=serializers.LocationsSerializers 


