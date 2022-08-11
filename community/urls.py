from django.urls import path, include
from .views import CommunityViewset, CommunityCommentsViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CommunityViewset)
com_router = DefaultRouter()
com_router.register('', CommunityCommentsViewset)

communitycomment_list = CommunityCommentsViewset.as_view({
    'get': 'list',
    'post': 'create',
})

communitycomment_detail = CommunityCommentsViewset.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'post': 'update',
})

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/comments/',communitycomment_list),
    path('<int:pk>/comments/<int:pk1>/',communitycomment_detail)
]