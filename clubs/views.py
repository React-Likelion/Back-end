import json
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from itertools import chain
from accounts.models import User
from .models import *
from .serializer import *

# import imgbbpy
# import urllib.request
# from react.settings import MEDIA_URL, MEDIA_ROOT


# 검색 필터 기능
def include_filter(queryset, request):
    request = dict(request)
    for key, vals in request.items():
        if key == 'popular':
            queryset = queryset.annotate(member_cnt=Count('member')).order_by('-member_cnt')
        
        # __contains loop를 통한 다중 필터링
        elif len(vals) == 1:
            queryset = queryset.filter(**{f"{key}__contains":vals[0]})
        else:
            queryset_list = []
            for val in vals:
                queryset_list.append(queryset.filter(**{f"{key}__contains":val}))
            
            queryset = queryset_list[0]
            for query in queryset_list[1:]:
                queryset = queryset | query
    return queryset


class ClubsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Clubs.objects.all().order_by('-id')

    serializer_class = ClubsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'field', 'location', 'age_group']

    @action(detail=True, method=['PATCH'])
    def patch_update(self, request, *args, **kwargs):
        # update overiding
        def update(request, *args, **kwargs):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            try:
                next_leader = User.objects.get(nickname=request.data['nickname'])
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            next_leader = next_leader.id
            # leader_id 변조 방지
            request.data._mutable = True
            request.data['leader_id'] = next_leader
            request.data._mutable = False

            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        kwargs['partial'] = True
        return update(request, *args, **kwargs)

    # filtering & sort 기능의 list
    @action(detail=False, method=['GET'])
    def club_list(self, request, *args, **kwargs):
        self.queryset = Clubs.objects.all().order_by('-id')
        # query들로 filter
        if request.query_params:
            self.queryset = include_filter(self.queryset, request.query_params)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    # sort 기능의 create 
    @action(detail=False, method=['POST'])
    def club_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        club = Clubs.objects.all().order_by('-id')[0] 
        new_club = ClubMembers(club_id=club)
        new_club.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, serializer):
        serializer.save()
        # img_hosting 레거시 코드
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
    
    #club 가입 & 탈퇴 기능
    # request에 out이 존재하면 탈퇴기능, 없으면 가입 기능으로 동작합니다.
    @action(detail=True, method=['POST'])
    def club_signin(self, request, **kwargs):
        club = self.queryset.filter(id=self.kwargs.get('pk'))[0]
        
        #sign_out이 존재 하지 않으면 None으로 처리.
        sign_id = request.data.get('id', None)
        sign_out = request.data.get('out', None)
        member_list = club.member.all()

        if sign_id is None:
            content = {'error': 'none_id'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        
        # 탈퇴 기능으로 처리할 경우
        if sign_out is not None:
            if User.objects.get(id=sign_id) in member_list:
                club.member.remove(request.data.get('id'))
                content = {'ok': 'signout complete!'}
                return Response(content, status=status.HTTP_200_OK)
            
            else:
                content = {'error': 'not register in club!'}
                return Response(content, status=status.HTTP_403_FORBIDDEN)
        # 가입 기능으로 처리할 경우
        else:
            if User.objects.get(id=sign_id) in member_list:
                content = {'error': 'already signed!'}
                return Response(content, status=status.HTTP_403_FORBIDDEN)
            
            club_member = ClubMembers.objects.filter(club_id__id=club.id)[0]
            if club_member.member_cnt >= club.limit:
                content = {'error': 'club is already full!'}
                return Response(content, status=status.HTTP_403_FORBIDDEN)
            
            club.member.add(request.data.get('id'))
            club.save()
            club_member.member_cnt += 1
            club_member.save()

            content = {'ok': 'singin complete!'}
            return Response(content, status=status.HTTP_200_OK)
    

#다중 이미지 업로드 수정
class ClubsArticleViewSet(ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Clubboard.objects.all()
    serializer_class = ClubBoardSerializer
        
    @action(detail=True, methods=['GET'])
    def article_list(self, request, **kwargs):
        article_query = self.queryset.filter(club_id=self.kwargs.get('club_pk', ''))

        if request.query_params:
            article_query = include_filter(article_query, request.query_params)

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
    
    @action(detail=True, methods=['GET'])
    def get_article(self, request, **kwargs):
        comment = self.queryset.filter(id=self.kwargs.get('pk'), club_id=self.kwargs.get('club_pk'))[0]
        serializer = self.get_serializer(comment)
        return Response(serializer.data)


class GalleriesViewSet(ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Galleries.objects.all()
    serializer_class = GalleriesSerializer

    # filtering 적용한 list
    @action(detail=True, methods=['GET'])
    def gallery_list(self, request, **kwargs):
        article_query = self.queryset.filter(club_id=self.kwargs.get('club_pk', ''))
        
        # query들로 filter 적용
        if request.query_params:
            article_query = include_filter(article_query, request.query_params)

        serializer = self.get_serializer(article_query, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['POST'])
    def gallery_create(self, request, **kwargs):
        # club_pk 변조방지
        request.data._mutable = True
        request.data['club_id'] = str(self.kwargs.get('club_pk', ''))
        request.data._mutable = False

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()
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
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Clubboard_comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['GET'])
    def get_comment(self, request, **kwargs):
        comment = self.queryset.filter(id=self.kwargs.get('comment_pk'), board_id=self.kwargs.get('pk'))
        
        # 최초 코멘트 일때, 대댓글 전부 chaining
        if not comment[0].parent:
            alpha_comment = self.queryset.filter(parent=comment[0].id)
            comment = list(chain(comment, alpha_comment))

        serializer = self.get_serializer(comment, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['GET'])
    def get_comment_list(self, request, **kwargs):
        comment = self.queryset.filter(board_id=self.kwargs.get('pk'))
        serializer = self.get_serializer(comment, many=True)
        return Response(serializer.data)
    
    

    
    """ @action(detail=True, methods=['POST'])
    def addcomment(self, request, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)"""



class ClubsNewViewSet(ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Clubs.objects.all().order_by('-id')
    serializer_class = ClubsSerializer


class ClubsMemberViewSet(ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Clubs.objects.all()\
                .annotate(member_cnt=Count('member'))\
                .order_by('-member_cnt')
    serializer_class = ClubsSerializer

class SignedClubViewSet(ModelViewSet):
    queryset = Clubs.objects.all()
    # 소속된 모든 clubs을 json으로 return
    @action(detail=True, methods=['GET'])
    def get_signed_club(self, request, **kwargs):
        join_clubs = []
        for club in self.queryset:
            member_list = club.member.all()
            if User.objects.get(id=self.kwargs.get('pk')) in member_list:
                join_clubs.append(club.id)
        data = {"joined":join_clubs}
        data = json.dumps(data)
        return Response(data=data)

class MakeClubViewSet(ModelViewSet):
    queryset = Clubs.objects.all()
    # 제작한 모든 clubs를 json으로 return
    @action(detail=True, methods=['GET'])
    def get_made_club(self, request, **kwargs):
        join_clubs = []
        for club in self.queryset:
            if User.objects.get(id=self.kwargs.get('pk')) == club.leader_id:
                join_clubs.append(club.id)
        data = {"made":join_clubs}
        data = json.dumps(data)
        return Response(data=data)

class MainViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Clubs.objects.all().order_by('-id')[:4]
    serializer_class = ClubsSerializer
    
 

clubs_list = ClubsViewSet.as_view({
    'get': 'club_list',
    'post': 'club_create',
})

signed_club = SignedClubViewSet.as_view({
    'get': 'get_signed_club'
})
made_club = MakeClubViewSet.as_view({
    'get': 'get_made_club'
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
    'patch': 'patch_update',
    'delete': 'destroy',

    'post': 'club_signin',
})

clubs_article_list = ClubsArticleViewSet.as_view({
    'get': 'article_list',
    'post': 'article_create',
})

clubs_article_detail = ClubsArticleViewSet.as_view({
    'get': 'get_article',
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

clubs_comments_detail = CommentViewSet.as_view({
    'get': 'get_comment',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

clubs_comments = CommentViewSet.as_view({
    'get': 'get_comment_list',
    'post': 'create',
})

main_list = MainViewSet.as_view({
    'get': 'list'
})
