from django.urls import path, include
from rest_framework import routers
from mentorings import views

router_mentor=routers.DefaultRouter()
router_chat=routers.DefaultRouter()
router_mentor.register('',views.MentoringViewSet)
router_chat.register('',views.Mentoring_ChatsViewSet)

urlpatterns=[
    #http://127.0.0.1:8000/mentorings/
    #http://127.0.0.1:8000/mentorings?title=&age_group=&location=&field=
    path('',include(router_mentor.urls)),
        
    #http://127.0.0.1:8000/mentorings/1/mentoring-chats/
    path('<int:pk>/mentoring-chats/', include(router_chat.urls)),    
]
