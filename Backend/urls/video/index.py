from django.urls import path,include
from Backend.views.video.list import ListView
from Backend.views.video.content import ContentView
urlpatterns = [
    path('list/', ListView.as_view(), name='video_list'),
    path('content/', ContentView.as_view(), name='video_content'),
]