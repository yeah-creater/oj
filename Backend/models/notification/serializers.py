from rest_framework import serializers
from Backend.models.user.serializers import UserInfoSerializer
from Backend.models.user.user import UserInfo
from Backend.models.notification.notification import Notification
class NotificationSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    target = serializers.SerializerMethodField()
    def get_target(self, obj):
        user_info = UserInfo.objects.get(user_id = obj.target.id)
        data = UserInfoSerializer(user_info).data
        return data
    class Meta:
        model = Notification
        fields = '__all__'



