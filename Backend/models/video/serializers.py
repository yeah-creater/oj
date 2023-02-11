from rest_framework import serializers
from Backend.models.video.video import Video
from Backend.models.user.user import UserInfo
import json


class VideoListSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = Video
        fields = ['id','user_id','title','create_time']

class VideoContentSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = Video
        fields = '__all__'