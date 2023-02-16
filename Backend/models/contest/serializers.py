from rest_framework import serializers
from Backend.models.contest.contest import Contest
from Backend.models.contest.contest import ContestParticipant
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoSerializer


class ContestSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    over_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return UserInfoSerializer(UserInfo.objects.get(user = obj.user)).data
    class Meta:
        model = Contest
        fields = '__all__'

class ContestParticipantSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return UserInfoSerializer(UserInfo.objects.get(user = obj.user)).data
    class Meta:
        model = ContestParticipant
        fields = '__all__'