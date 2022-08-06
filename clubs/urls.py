from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.clubs_list),
    path('<int:pk>/', views.clubs_detail),
    path('by-newset/', views.clubs_new_list),
    path('by-member/', views.clubs_member_list),
]