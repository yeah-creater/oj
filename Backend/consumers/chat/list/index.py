from channels.generic.websocket import AsyncWebsocketConsumer
from Backend.models.chat.chat import ChatMessage
from Backend.models.chat.serializers import ChatMessageSerializer
import json
from django.core.cache import cache
class List(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if  self.user.is_authenticated:
            self.room_name = str(self.user.id)
            await self.accept()
            print('accept')
            await self.channel_layer.group_add(self.room_name, self.channel_name)
        else:
            print('用户未登录')
    async def disconnect(self, close_code):
        print('disconnect')
        if hasattr(self,'room_name'):
            await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data['event']
        # 更新target的chatlist
        if event == 'message':
            target = data['target']
            await self.channel_layer.group_send(
            str(target),
            {
                'type':'group_send_event',
                'event':'message',
            }
            )

    async def group_send_event(self,data):
        await self.send(text_data = json.dumps(data)) # json.dumps :将json字典转化为字符串