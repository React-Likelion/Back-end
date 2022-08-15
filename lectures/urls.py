from django.urls import path, include
from .views import LecturesViewSet, LecturesEnrollViewSet, LecturesLikeViewSet
from rest_framework.routers import DefaultRouter

#라우팅 설정
lectures_router = DefaultRouter()
lectures_router.register('', LecturesViewSet)


lectures_list = LecturesViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


lectures_detail = LecturesViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'post': 'update',
})

lectures_enroll = LecturesEnrollViewSet.as_view({
    'patch': 'update',
})

lectures_like = LecturesLikeViewSet.as_view({
    'patch': 'update',
})

urlpatterns =[
    path('', include(lectures_router.urls)),
    path('<int:pk>/enroll/',lectures_enroll),
    path('<int:pk>/like/',lectures_like),

] 