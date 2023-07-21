
from django.urls import path
from . import views

urlpatterns = [    
    path('',views.Home,name='home'),
    path('login', views.UserLogin, name='login'),
    path('regist',views.userSignUp, name='register'),
    path('logout',views.userLogout, name='logout'),
    path('profile/<str:pk>',views.userProfile, name='user_profile'),
    


    path('room/<str:pk>',views.room,name='room'),
    path('create-room',views.CreateRoom,name='create-room'),
    path('update-room/<str:pk>',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.deleteRoom,name='delete-room'),
    path('delete-message/<str:pk>',views.deleteMessage,name='delete-message'),
]