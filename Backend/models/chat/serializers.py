from rest_framework import serializers
from Backend.models.chat.chat import ChatList
from Backend.models.chat.chat import ChatMessage
from Backend.models.user.serializers import UserInfoSerializer
from Backend.models.user.user import UserInfo
from django.core.cache import cache
class ChatListSerializer(serializers.ModelSerializer):
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    target = serializers.SerializerMethodField()
    unread = serializers.SerializerMethodField()
    def get_unread(self, obj):
        room_name = str(obj.source.id) + 'from' + str(obj.target.id)
        if not cache.has_key(room_name):
            cache.set(room_name, 0)
            return 0
        else:
            return cache.get(room_name)
    def get_target(self, obj):
        user_info = UserInfo.objects.get(user_id = obj.target.id)
        data = UserInfoSerializer(user_info).data
        return data
    class Meta:
        model = ChatList
        fields = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    source = serializers.SerializerMethodField()
    target = serializers.SerializerMethodField()
    def get_target(self, obj):
        user_info = UserInfo.objects.get(user_id = obj.target.id)
        data = UserInfoSerializer(user_info).data
        return data
    def get_source(self, obj):
        user_info = UserInfo.objects.get(user_id = obj.source.id)
        data = UserInfoSerializer(user_info).data
        return data
    class Meta:
        model = ChatMessage
        fields = '__all__'


