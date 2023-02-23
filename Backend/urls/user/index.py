from django.urls import path,include
from Backend.views.user.user_info import UserInfoView
from Backend.views.user.follow import FollowView
from Backend.views.user.profile import ProfileView
from Backend.views.user.follows import FollowsView
from Backend.views.user.notification import NotificationView
urlpatterns = [
    path('user_info/', UserInfoView.as_view(), name='user_user_info'),
    path('follow/',FollowView.as_view(),name='user_follow'),
    path('profile/',ProfileView.as_view(),name='user_profile'),
    path('follows/',FollowsView.as_view(),name='user_follows'),
    path('notification/',NotificationView.as_view(),name='user_notification'),
]