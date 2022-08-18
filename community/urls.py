from django.urls import path, include
from .views import CommunityViewset, CommunityCommentsViewset, MainPageViewset, NoticeViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CommunityViewset)
com_router = DefaultRouter()
com_router.register('', CommunityCommentsViewset)

community_list = CommunityViewset.as_view({
    'get': 'list',
    'post': 'create',
})

community_detail = CommunityViewset.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'post': 'update',
})


communitycomment_list = CommunityCommentsViewset.as_view({
    'get': 'list',
    'post': 'create',
})

communitycomment_detail = CommunityCommentsViewset.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'put': 'update',
})

mainpage_list = MainPageViewset.as_view({
    'get': 'list',
})

notice_list = NoticeViewset.as_view({
    'get': 'list',
})


urlpatterns = [
    path('',community_list),
    path('<int:pk>/',community_detail),

    path('main/', mainpage_list),
    path('notice/', notice_list),

    path('<int:pk>/comments/',communitycomment_list),
    path('<int:pk>/comments/<int:pk1>/',communitycomment_detail)
]
