from rest_framework import serializers
from Backend.models.user.user import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format='%Y-%m-%d', input_formats=None)
    class Meta:
        model = UserInfo
        fields = '__all__'

class UserInfoRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id','name','photo','rating']


