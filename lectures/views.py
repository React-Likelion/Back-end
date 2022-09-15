from .models import Lectures
from accounts.models import User, Logs
from .serializers import LecturesSerializer

from django.shortcuts import get_object_or_404
from django.db.models import F, Q

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# lecture
class LecturesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    # 강의 등록 시 포인트 지급
    def perform_create(self, serializer):
        serializer.save()
        User.objects.filter(nickname=self.request.user).update(point=F('point')+1000)
        point = Logs(plus_log='+1000')
        point.save()
        queryset = User.objects.filter(nickname=self.request.user)
        insert = get_object_or_404(queryset)
        insert.log.add(Logs.objects.latest('id'))
        #print(User.objects.filter(nickname=self.request.user))


    def list(self, request):
        '''
        < 리스트 정렬 querystring >
        ?sort = 정렬 하고 싶은 것 (오름차순은 앞에 - 붙일 것!)
            ex) https://port-0-back-end-14q6cqs24l6kns2t6.gksl1.cloudtype.app/lectures/?sort=-visit_cnt
        '''
        if (request.GET.get('sort') != None):
            sort = request.GET.get('sort')
            # 생성시간의 오름차순 리스트를 default로 설정
            data = Lectures.objects.all().order_by(sort,'-create_date')
        else:
            data = Lectures.objects.all().order_by('-create_date')
        title = request.GET.getlist('title')
        main_category = request.GET.getlist('main_category')
        sub_category = request.GET.getlist('sub_category')

        '''
        < 검색 기능 >
        ?search_list = {search_value}
            ex) https://port-0-back-end-14q6cqs24l6kns2t6.gksl1.cloudtype.app/lectures/?main_category=외국어
        '''
        search_list = {"title":title, "main_category":main_category, "sub_category":sub_category}
        q = Q()

        for key in search_list:
            if search_list[key]:
                if key == "title":
                    q.add(Q(title__in=title), q.AND)
                elif key == "main_category":
                    q.add(Q(main_category__in=main_category), q.AND)
                else:
                    q.add(Q(sub_category__in=sub_category), q.AND)
        queryset = data.filter(q)
        serializer = LecturesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 강의를 조회하면 조회수 증가
    def retrieve(self, request, pk=None):
        view = Lectures.objects.get(id = pk)
        view.visit_cnt += 1 
        view.save()      
        data = self.serializer_class(view).data
        
        return Response(data, status=status.HTTP_202_ACCEPTED)

# 강의 등록 리스트
class LecturesEnrollViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    # 강의 수강 신청 
    def update(self, request, pk=None):
        queryset = Lectures.objects.all()

        if request.user.is_authenticated:
            lectures = get_object_or_404(queryset, id=pk)
            #print(lectures)
            # 강의 수강 취소
            if lectures.enroll_students.filter(pk=request.user.pk).exists():
                lectures.enroll_students.remove(request.user)
                Lectures.objects.filter(id=pk).update(enroll_cnt=F('enroll_cnt')-1)
            else:
                # 강의 수강 신청 및 포인트 결제
                lectures.enroll_students.add(request.user)
                Lectures.objects.filter(id=pk).update(enroll_cnt=F('enroll_cnt')+1)
                prices = Lectures.objects.get(id=pk).price
                #print(prices)
                print(User.objects.filter(nickname=request.user))
                User.objects.filter(nickname=request.user).update(point=F('point')-prices)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# 강의 좋아요 
class LecturesLikeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def update(self, request, pk=None):
        queryset = Lectures.objects.all()

        if request.user.is_authenticated:
            lectures = get_object_or_404(queryset, id=pk)

            if lectures.like_members.filter(pk=request.user.pk).exists():
                # 강의 좋아요 취소
                lectures.like_members.remove(request.user)
                Lectures.objects.filter(id=pk).update(like_cnt=F('like_cnt')-1)
            else:
                # 강의 좋아요 
                lectures.like_members.add(request.user)
                Lectures.objects.filter(id=pk).update(like_cnt=F('like_cnt')+1)
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# 마이페이지에 보여질 내가 등록한 강의 리스트
class MypageViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def list(self, request):
        # 생성시간의 오름차순 리스트를 default로 설정
        queryset = self.get_queryset().filter(writer_nickname=self.request.user).order_by('-id')
        #print(self.request.user)
        serializer = LecturesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
# 마이페이지에 보여질 내가 수강 중인 강의 리스트
class MypageLecturesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def list(self, request):
        # 생성시간의 오름차순 리스트를 default로 설정
        queryset = Lectures.objects.filter(enroll_students__in=[self.request.user]).exclude(writer_nickname=self.request.user).order_by('-id')
        serializer = LecturesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# 메인페이지에 보여질 강의 리스트
class MainPageViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def list(self, request):
        queryset = Lectures.objects.order_by('-like_cnt')[:4]
        serializer = LecturesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
