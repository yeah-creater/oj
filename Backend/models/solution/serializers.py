from rest_framework import serializers
from Backend.models.solution.solution import Solution
from Backend.models.user.user import UserInfo
import json

class SolutionSearchSerializer(serializers.ModelSerializer):
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
        model = Solution
        fields = ['id','user_id','problem','title','create_time']

class SolutionListSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = Solution
        fields = ['id','user_id','problem','title','create_time']

class SolutionContentSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = Solution
        fields = '__all__'