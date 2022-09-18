from django.urls import path, include
from .views import CommunityViewset, CommunityCommentsViewset
from rest_framework.routers import DefaultRouter

# Community 라우터
router = DefaultRouter()
router.register('', CommunityViewset)
# Community 댓글 라우터
com_router = DefaultRouter()
com_router.register('', CommunityCommentsViewset)


# Community method
""" community_list = CommunityViewset.as_view({
    'get': 'list',
    'post': 'create',
})

community_detail = CommunityViewset.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'patch': 'partial_update',
})

# Community comment method
communitycomment_list = CommunityCommentsViewset.as_view({
    'get': 'list',
    'post': 'create',
})

communitycomment_detail = CommunityCommentsViewset.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'patch': 'partial_update',
})


# 메인페이지 
mainpage_list = MainPageViewset.as_view({
    'get': 'list',
})


# 공지사항 
notice_list = NoticeViewset.as_view({
    'get': 'list',
})
""" 

urlpatterns = [
    path('',include(router.urls)), #Community
        
    path('<int:pk>/comments/', include(com_router.urls)),    # Community 댓글
    # path('',community_list),
    # path('<int:pk>/',community_detail),

    # path('main/', mainpage_list), # 메인페이지에 보여질 게시글
    # path('notice/', notice_list), # Community 상단에 고정되어 보여질 공지사항 게시글

    # path('<int:pk>/comments/',communitycomment_list),
    # path('<int:pk>/comments/<int:pk1>/',communitycomment_detail)
]
