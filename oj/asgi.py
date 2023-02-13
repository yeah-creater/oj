"""
ASGI config for oj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oj.settings')
django.setup()
from Backend.channelsmiddleware import JwtAuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from Backend.routing import websocket_urlpatterns

from channels.layers import get_channel_layer
channel_layer = get_channel_layer()  # 实现服务器端进程向客户端调用函数

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JwtAuthMiddlewareStack(URLRouter(websocket_urlpatterns))
})