from .serializers import CommunitySerializers, CommunityCommentsSerializers
from .models import Community, CommunityComments

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

# Community 
class CommunityViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    # 생성시간의 오름차순 리스트를 default로 설정
    queryset = Community.objects.all().order_by('-create_time') 
    serializer_class = CommunitySerializers
    # 검색기능('제목', '내용', '카테고리', '작성자')
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['title', 'description', 'category','writer_id']

    # 메인페이지에 보여질 5개의 최신 게시글 List
    @action(detail=False)
    def main(self, request):
        queryset = self.get_queryset().order_by('-id')[:5]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# Community 댓글
class CommunityCommentsViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CommunityComments.objects.all()
    serializer_class = CommunityCommentsSerializers

    def list(self, request, pk=None):
        queryset = CommunityComments.objects.filter(board_id=pk)
        serializer = CommunityCommentsSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 속 댓글의 수 구현
    def perform_create(self, serializer):
        serializer.save()
        count_comments = CommunityComments.objects.filter(board_id=serializer.data.get('board_id')).count()
        #print (count_comments)
        Community.objects.filter(id=serializer.data.get('board_id')).update(comment_cnt=count_comments)


    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
""" 
# 메인페이지
class MainPageViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all().order_by('-create_time')[:5]
    serializer_class = CommunitySerializers
 """

# 게시판 상단에 최신의 공지사항 3개 고정 출력
class NoticeViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all().order_by('-create_time')[:3]
    serializer_class = CommunitySerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['category']
""" 
    def retrieve(self, request, pk=None, pk1= None):
        queryset = CommunityComments.objects.filter(board_id=pk).filter(id=pk1)
        serializer = CommunityCommentsSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 """
