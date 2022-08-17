from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ClubsViewSet


urlpatterns = [
    path('', views.clubs_list),
    path('signed/<int:pk>/', views.signed_club),
    path('made/<int:pk>/', views.made_club),
   
    path('by-newset/', views.clubs_new_list),
    path('by-member/', views.clubs_member_list),
    
    path('<int:pk>/', views.clubs_detail), 
    path('<int:club_pk>/articles/', views.clubs_article_list), 
    path('<int:club_pk>/articles/<int:pk>/', views.clubs_article_detail),
    path('<int:club_pk>/articles/<int:pk>/comment/', views.clubs_comments),
    path('<int:club_pk>/articles/<int:pk>/comment/<int:comment_pk>', views.clubs_comments_detail),

    path('<int:club_pk>/galleries/', views.clubs_galleries_list), 
    path('<int:club_pk>/galleries/<int:pk>/', views.clubs_galleries_detail),
]