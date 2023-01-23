from django.urls import path
from Backend.consumers.chat.index import Chat

# 类似http的路由
websocket_urlpatterns = [
    path('wss/chat/',Chat.as_asgi(),name="wss_chat"),

]