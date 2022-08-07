from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.clubs_list),
   
    path('by-newset/', views.clubs_new_list),
    path('by-member/', views.clubs_member_list),
    
    path('<int:pk>/', views.clubs_detail), 
    path('<int:pk>/articles/', views.clubs_detail), 
    #path('<int:pk>/articles/<int:pk_2>', views.clubs_detail),

    #path('<int:pk>/galleries', views.clubs_detail), 
    #path('<int:pk>/galleries/<int:pk_2>', views.clubs_detail), 
]