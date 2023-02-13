from channels.generic.websocket import AsyncWebsocketConsumer
from Backend.models.chat.chat import ChatMessage
from Backend.models.chat.serializers import ChatMessageSerializer
import json
from django.core.cache import cache
class Chat(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if  self.user.is_authenticated:
            await self.accept()
            print('accept')
            # await self.channel_layer.group_add(self.room_name, self.channel_name)
        else:
            print('用户未登录')
    async def disconnect(self, close_code):
        print('disconnect')
        if hasattr(self,'room_name'):
            await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data['event']
        # 刚打开聊天页面
        if event == 'init':
            source = self.user.id
            target = data['target']
            # 创建2个人专属的房间号=> room min_max 之前的数据交给http请求返回
            self.room_name = str(min(source,target)) + '-' + str(max(source,target))
            # 's'from't'的未读列表清零
            name = str(source)+'from'+str(target)
            cache.set(name, 0)
            await self.channel_layer.group_add(self.room_name, self.channel_name)
        # 发送消息
        elif event == 'message':
            source = self.user.id
            target = data['target']
            content = data['content']
            t_room_name = str(min(source,target)) + '-' + str(max(source,target))
            name = str(target) + 'from' + str(source)
            # 更新's'from't'的未读列表
            if not cache.has_key(name):
                cache.set(name, 0)
            cnt = cache.get(name)
            cache.set(name,cnt + 1)
            await self.channel_layer.group_send(
            t_room_name,
            {
                'type':'group_send_event',
                'event':'message',
                'id': source,
                'name': data['name'],
                'photo': data['photo'],
                'content': data['content'],
                'create_time': data['create_time']
            }
            )


    async def group_send_event(self,data):
        await self.send(text_data = json.dumps(data)) # json.dumps :将json字典转化为字符串