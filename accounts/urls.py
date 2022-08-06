from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import MembersListView, SignupView, UserActivate, LoginView

#router = routers.DefaultRouter()
#router.register(r'signup', SignupViewSet)
app_name = 'accounts'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', MembersListView.as_view(), name='members_list'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<str:uidb64>/<str:token>/', UserActivate.as_view(), name="activate"),
    #path('', include(router.urls))
]