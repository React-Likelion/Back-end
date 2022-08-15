from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import UserListView, SignupView, UserActivate, LoginView, UserUpdateView

#router = routers.DefaultRouter()
#router.register(r'signup', SignupViewSet)
app_name = 'accounts'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', UserListView.as_view(), name='user_list'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<str:uidb64>/<str:token>/', UserActivate.as_view(), name="activate"),
    #path('', include(router.urls))
]