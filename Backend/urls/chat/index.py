from django.urls import path,include
from Backend.views.chat.list import ListView
from Backend.views.chat.message import MessageView
urlpatterns = [
    path('list/', ListView.as_view(), name='chat_list'),
    path('message/', MessageView.as_view(), name='chat_message'),
]