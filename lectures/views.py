from django.shortcuts import get_object_or_404
from django.db.models import F, Q
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .serializers import LecturesSerializer
from .models import Lectures
from accounts.models import User, Logs


class LecturesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

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
        if (request.GET.get('sort') != None):
            sort = request.GET.get('sort')
            data = Lectures.objects.all().order_by(sort,'-create_date')
        else:
            data = Lectures.objects.all().order_by('-create_date')
        title = request.GET.getlist('title')
        main_category = request.GET.getlist('main_category')
        sub_category = request.GET.getlist('sub_category')

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

    def retrieve(self, request, pk=None):
        view = Lectures.objects.get(id = pk)
        view.visit_cnt += 1 
        view.save()      
        data = self.serializer_class(view).data
        
        return Response(data, status=status.HTTP_202_ACCEPTED)


class LecturesEnrollViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def update(self, request, pk=None):
        queryset = Lectures.objects.all()

        if request.user.is_authenticated:
            lectures = get_object_or_404(queryset, id=pk)
            #print(lectures)
            if lectures.enroll_students.filter(pk=request.user.pk).exists():
                lectures.enroll_students.remove(request.user)
                Lectures.objects.filter(id=pk).update(enroll_cnt=F('enroll_cnt')-1)
            else:
                lectures.enroll_students.add(request.user)
                Lectures.objects.filter(id=pk).update(enroll_cnt=F('enroll_cnt')+1)
                prices = Lectures.objects.get(id=pk).price
                #print(prices)
                print(User.objects.filter(nickname=request.user))
                User.objects.filter(nickname=request.user).update(point=F('point')-prices)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class LecturesLikeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def update(self, request, pk=None):
        queryset = Lectures.objects.all()

        if request.user.is_authenticated:
            lectures = get_object_or_404(queryset, id=pk)

            if lectures.like_members.filter(pk=request.user.pk).exists():
                lectures.like_members.remove(request.user)
                Lectures.objects.filter(id=pk).update(like_cnt=F('like_cnt')-1)
            else:
                lectures.like_members.add(request.user)
                Lectures.objects.filter(id=pk).update(like_cnt=F('like_cnt')+1)
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class MypageViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def list(self, request):
        queryset = self.get_queryset().filter(writer_nickname=self.request.user).order_by('-id')
        #print(self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
class MypageLecturesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def list(self, request):
        queryset = Lectures.objects.filter(enroll_students__in=[self.request.user]).exclude(writer_nickname=self.request.user).order_by('-id')
        serializer_class = LecturesSerializer
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
class MainPageViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

    def list(self, request):
        queryset = Lectures.objects.order_by('-like_cnt')[:4]
        serializer_class = LecturesSerializer
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
