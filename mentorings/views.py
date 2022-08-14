from mentorings import models, serializers
from accounts.models import User
from mentorings.models import mentorings, mentoring_chats
from rest_framework import viewsets
from rest_framework.response import Response
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.shortcuts import redirect
from django.db.models import Q

#멘토링 CRUD
class MentoringViewSet(viewsets.ModelViewSet):
    #permission_classes = [AllowAny,]
    queryset=mentorings.objects.all().order_by('-create_date')
    serializer_class=serializers.MentoringSerializers
    permission_classes=[IsAuthenticatedOrReadOnly]
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields=['title', 'age_group', 'location', 'field']

    def get_queryset(self):
        queryset=mentorings.objects.all()
        location=self.request.GET.getlist('location',None)
        limit=self.request.GET.getlist('limit',None)
        age_group=self.request.GET.getlist('age_group',None)
        field=self.request.GET.getlist('field',None)
        title=self.request.GET.get('title',None)
        
        filter_condition = Q()

        if location:
            filter_condition.add(Q(location__in=location), Q.AND)

        if limit:
            filter_condition.add(Q(limit__in=limit), Q.AND)

        if age_group:
            filter_condition.add(Q(age_group__in=age_group), Q.AND)
        
        if field:
            filter_condition.add(Q(field__in=field), Q.AND)

        if title:
            filter_condition.add(Q(title=title), Q.AND)

        queryset = queryset.filter(filter_condition).distinct().order_by('-create_date')
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        serializer.save(member_cnt=1)
        serializer.save(nickname=self.request.user.nickname)                
        
    @action(detail=False)    
    def listbycnt(self, request, *args, **kwargs):
        queryset = mentorings.objects.all().order_by('-member_cnt' , '-create_date')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    
        

#멘토링 챗 CRUD    
class Mentoring_ChatsViewSet(viewsets.ModelViewSet):
    #permission_classes = [AllowAny,]
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
        mentoring.member_cnt=mentoring_member[pk-1].count+1
        mentoring.save()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def withdraw(self, request, pk, *args, **kwargs):
        mentoring=get_object_or_404(mentorings,id=pk)
        print(mentoring)
        member=get_object_or_404(User, nickname=request.user)
        print(member)
        #manytomany테이블에서 삭제
        mentoring.User.remove(member)
        #인원수 감소
        mentoring_member=mentorings.objects.annotate(count=Count('User'))
        mentoring.member_cnt=mentoring_member[pk-1].count+1
        mentoring.save()
        return redirect('/mentorings')
