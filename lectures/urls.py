from django.urls import path, include
from .views import LecturesViewSet, LecturesEnrollViewSet, LecturesLikeViewSet, MypageViewSet, MypageLecturesViewSet, MainPageViewSet
from rest_framework.routers import DefaultRouter

""" 
#라우팅 설정
lectures_router = DefaultRouter()
lectures_router.register('', LecturesViewSet)
 """

# 강의 전체 리스트
lectures_list = LecturesViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

# 강의 세부 리스트
lectures_detail = LecturesViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'patch': 'update',
})

# 강의 수강 학생 등록
lectures_enroll = LecturesEnrollViewSet.as_view({
    'patch': 'update',
})

# 강의 좋아요 등록
lectures_like = LecturesLikeViewSet.as_view({
    'patch': 'update',
})

# 마이페이지에 보여질 내가 등록한 강의 리스트
mypage_list = MypageViewSet.as_view({
    'get': 'list',
})

# 마이페이지에 보여질 내가 수강 중인 강의 리스트
mypagelectures_list = MypageLecturesViewSet.as_view({
    'get': 'list',
})

# 메인페이지에 보여질 강의 리스트
main_list = MainPageViewSet.as_view({
    'get': 'list',
})



urlpatterns =[

    #path('', include(lectures_router.urls)),
    path('', lectures_list), # 강의 전체 리스트
    path('<int:pk>/', lectures_detail), # 강의 세부 리스트
    path('mypage/', mypage_list), # 마이페이지에 보여질 내가 등록한 강의 리스트
    path('mypagelectures/', mypagelectures_list), # 마이페이지에 보여질 내가 수강 중인 강의 리스트
    path('main/', main_list), # 메인페이지에 보여질 강의 리스트
    path('<int:pk>/enroll/',lectures_enroll), # 강의 수강 학생 등록 
    path('<int:pk>/like/',lectures_like), # 강의 좋아요 등록
    
] 
