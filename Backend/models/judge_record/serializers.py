from rest_framework import serializers
from Backend.models.judge_record.judge_record import SubmitRecord
from Backend.models.judge_record.judge_record import DebugRecord


class SubmitRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeRecord
        fields = '__all__'
class DebugRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeRecord
        fields = '__all__'