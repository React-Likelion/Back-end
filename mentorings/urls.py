from django.urls import path, include
from rest_framework import routers
from mentorings import views

router_mentor=routers.DefaultRouter()
router_chat=routers.DefaultRouter()
router_mentor.register('',views.MentoringViewSet)
router_chat.register('',views.Mentoring_ChatsViewSet)

urlpatterns=[
    path('',include(router_mentor.urls)),
    path('<int:pk>/mentoring-chats/', include(router_chat.urls))
]
