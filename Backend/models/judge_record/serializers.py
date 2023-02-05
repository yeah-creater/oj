from rest_framework import serializers
from Backend.models.judge_record.judge_record import SubmitRecord
from Backend.models.judge_record.judge_record import DebugRecord


class SubmitRecordSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = SubmitRecord
        fields = '__all__'
class SubmitRecordListSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = SubmitRecord
        fields = ['id','language','status','time']
class DebugRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebugRecord
        fields = '__all__'