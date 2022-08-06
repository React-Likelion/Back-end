from django.urls import path, include
from . import views
from rest_framework import routers
#from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import SignupView, LoginView

#router = routers.DefaultRouter()
#router.register(r'signup', MembersViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('', include(router.urls))
]