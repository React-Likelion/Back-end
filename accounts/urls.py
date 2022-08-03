from django.urls import path, include
from rest_framework import routers

from accounts.views import MembersViewSet

router = routers.DefaultRouter()
router.register(r'users', MembersViewSet)

urlpatterns = [
    path('', include(router.urls))
]