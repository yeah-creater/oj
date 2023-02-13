from django.urls import path
from Backend.consumers.chat.index import Chat
from Backend.consumers.chat.list.index import List

# 类似http的路由
websocket_urlpatterns = [
    path('wss/chat/',Chat.as_asgi(),name="wss_chat"),
    path('wss/chat/list/',List.as_asgi(),name="wss_chat_list")

]