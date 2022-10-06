from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views

from accounts.views import UserListView, SignupView, UserActivate, LoginView, PointViewSet, UserPointView, UserUpdateView, UserDetailViewSet

#라우팅 설정
router = DefaultRouter()
router.register('', PointViewSet)
detailrouter = DefaultRouter()
detailrouter.register('', UserDetailViewSet)
#router = routers.DefaultRouter()
#router.register(r'signup', SignupViewSet)
app_name = 'accounts'


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', include(detailrouter.urls), name='detail'),
    #path('<int:pk>/', views.user_detail, name='user_detail'),  
    path('signup/', SignupView.as_view(), name='signup'),
    #path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<str:uidb64>/<str:token>/', UserActivate.as_view(), name="activate"),
    path('point/', UserPointView.as_view(), name='point'),
    path('pointlog/', include(router.urls), name='pointlog')
    #path('point/', point_list)
    #path('', include(router.urls))
]
