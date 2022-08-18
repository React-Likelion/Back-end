from unicodedata import category
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import CommunitySerializers, CommunityCommentsSerializers, MainPageSerializer
from .models import Community, CommunityComments
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

class CommunityViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all().order_by('-create_time')
    serializer_class = CommunitySerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['title', 'description', 'category']

class CommunityCommentsViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CommunityComments.objects.all()
    serializer_class = CommunityCommentsSerializers

    def perform_create(self, serializer):
        serializer.save()
        count_comments = CommunityComments.objects.filter(board_id=serializer.data.get('board_id')).count()
        #print (count_comments)
        Community.objects.filter(id=serializer.data.get('board_id')).update(comment_cnt=count_comments)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MainPageViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all().order_by('-create_time')[:5]
    serializer_class = MainPageSerializer

class NoticeViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all().order_by('-create_time')[:3]
    serializer_class = CommunitySerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['category']