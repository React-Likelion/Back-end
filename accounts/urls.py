from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views

from accounts.views import UserViewSet, UserActivate, PointViewSet, UserPointView
#라우팅 설정
router = DefaultRouter()
router.register('', PointViewSet)

user_router = DefaultRouter()
user_router.register('', UserViewSet)

# login_router = DefaultRouter()
# login_router.register('', LoginViewSet)

app_name = 'accounts'


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(user_router.urls), name='user'),
    path('<int:pk>/update/', views.user_update, name='user_update'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<str:uidb64>/<str:token>/', UserActivate.as_view(), name="activate"),
    path('point/', UserPointView.as_view(), name='point'),
    path('pointlog/', include(router.urls), name='pointlog')
    #path('login/', views.login, name='login'),  
    #path('login/', include(login_router.urls), name='login'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    #path('signup/', SignupView.as_view(), name='signup'),
    #path('', UserListView.as_view(), name='user_list'),
    #path('point/', point_list)
    #path('', include(router.urls))
]

# accounts/   ->   User List, Sign Up
# accounts/{id}/   ->   User Detail, Delete
# accounts/{id}/update/   ->   User Update