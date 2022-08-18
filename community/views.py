from unicodedata import category
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import CommunitySerializers, CommunityCommentsSerializers
from .models import Community, CommunityComments
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

class CommunityViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all().order_by('-create_time')
    serializer_class = CommunitySerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['title', 'description', 'category','writer_id']

    @action(detail=False)
    def main(self, request):
        queryset = self.get_queryset().order_by('-id')[:5]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CommunityCommentsViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CommunityComments.objects.all()
    serializer_class = CommunityCommentsSerializers

    def list(self, request, pk=None):
        queryset = CommunityComments.objects.filter(board_id=pk)
        serializer = CommunityCommentsSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
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
    serializer_class = CommunitySerializers

class NoticeViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all().order_by('-create_time')[:3]
    serializer_class = CommunitySerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['category']

    # def retrieve(self, request, pk=None, pk1= None):
    #     queryset = CommunityComments.objects.filter(board_id=pk).filter(id=pk1)
    #     serializer = CommunityCommentsSerializers(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

