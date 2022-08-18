from django.urls import path, include
from .views import LecturesViewSet, LecturesEnrollViewSet, LecturesLikeViewSet, MypageViewSet, MypageLecturesViewSet, MainPageViewSet
from rest_framework.routers import DefaultRouter

#라우팅 설정
lectures_router = DefaultRouter()
lectures_router.register('', LecturesViewSet)


lectures_list = LecturesViewSet.as_view({
    'get': 'list',
    'post': 'perform_create',
})

lectures_detail = LecturesViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'patch': 'update',
})

lectures_enroll = LecturesEnrollViewSet.as_view({
    'patch': 'update',
})

lectures_like = LecturesLikeViewSet.as_view({
    'patch': 'update',
})

mypage_list = MypageViewSet.as_view({
    'get': 'list',
})

mypagelectures_list = MypageLecturesViewSet.as_view({
    'get': 'list',
})

main_list = MainPageViewSet.as_view({
    'get': 'list',
})



urlpatterns =[
    path('', lectures_list),
    path('<int:pk>/', lectures_detail),
    path('mypage/', mypage_list),
    path('mypagelectures/', mypagelectures_list),
    path('main/', main_list),
    path('<int:pk>/enroll/',lectures_enroll),
    path('<int:pk>/like/',lectures_like),
    

] 
