from django.urls import path,include
from Backend.views.video.list import ListView
from Backend.views.video.content import ContentView
from Backend.views.video.upload_video import UploadVideoView
urlpatterns = [
    path('list/', ListView.as_view(), name='video_list'),
    path('content/', ContentView.as_view(), name='video_content'),
    path('upload_video/', UploadVideoView.as_view(), name='video_upload_video'),
]