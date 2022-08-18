from mentorings import models, serializers
from accounts.models import User
from mentorings.models import mentorings, mentoring_chats
from rest_framework import viewsets
from rest_framework.response import Response
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.shortcuts import redirect
from django.db.models import Q
# import imgbbpy
# import urllib.request
# from react.settings import MEDIA_URL, MEDIA_ROOT

#멘토링 CRUD
class MentoringViewSet(viewsets.ModelViewSet):
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
        popular=self.request.GET.get('popular',None)
        
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
            
        if popular:
            queryset = queryset.filter(filter_condition).distinct().order_by('-member_cnt', '-create_date')
            
        else:
            queryset = queryset.filter(filter_condition).distinct().order_by('-create_date')
        
        return queryset
    
    def perform_create(self, serializer):
        temp=[]
        member=get_object_or_404(User, nickname=self.request.user)
        temp+=[member]
        serializer.save(User=temp)        
        serializer.save(user_id=self.request.user)
        serializer.save(member_cnt=1)
        serializer.save(nickname=self.request.user.nickname)         
        
#         data=serializer.save()        
#         client = imgbbpy.SyncClient('2e06ba182c51139ee0f81b7cfd52181c')
#         temp=data.image
#         root='http://127.0.0.1:8000'+MEDIA_URL
#         path=root+str(temp)
#         #tempmediaroot=str(MEDIA_ROOT)
#         pathtemp='media/a.jpg'
#         print(f"path: {path}, pathtemp: {pathtemp}")
#         print('111111111111111111111111111111')
#         urllib.request.urlretrieve(path, pathtemp)
#         image = client.upload(file=pathtemp)
#         print(image.url)
        
#         serializer.save(imageurl=image.url)     
        
        
    @action(detail=False)    
    def listbycnt(self, request, *args, **kwargs):
        queryset = mentorings.objects.all().order_by('-member_cnt','-create_date')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False)        
    def make(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        writer=request.user.nickname
        queryset=queryset.filter(nickname=writer)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    @action(detail=False)    
    def register(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        user_id=request.user.id
        nickname=request.user.nickname
        print(user_id)
        queryset = queryset.filter(User__in=[user_id]).exclude(nickname=nickname)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    

    @action(detail=False)
    def main(self, request):
        queryset = self.get_queryset().order_by('-id')[:4]
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
        mentoring_member=mentorings.objects.annotate(count=Count('User')).filter(id=pk)
        mentoring.member_cnt=mentoring_member[0].count
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
        member=get_object_or_404(User, nickname=request.user)
        #manytomany테이블에서 삭제
        mentoring.User.remove(member)
        #인원수 감소
        mentoring_member=mentorings.objects.annotate(count=Count('User')).filter(id=pk)
        mentoring.member_cnt=mentoring_member[0].count
        return redirect('/mentorings')
