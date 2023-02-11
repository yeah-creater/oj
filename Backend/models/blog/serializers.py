from rest_framework import serializers
from Backend.models.blog.blog import Blog
from Backend.models.user.user import UserInfo
import json

class BlogSearchSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    user_id = serializers.SerializerMethodField()
    def get_user_id(self, obj):
        user_info = UserInfo.objects.get(user_id = obj.user_id)
        return json.dumps({
            'user_id':obj.user_id,
            'user_info_name':user_info.name,
            'user_info_photo':user_info.photo,
        })
    class Meta:
        model = Blog
        fields = ['id','user_id','title','create_time']

class BlogListSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = Blog
        fields = ['id','user_id','title','create_time']

class BlogContentSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = Blog
        fields = '__all__'

