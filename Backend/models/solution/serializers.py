from rest_framework import serializers
from Backend.models.solution.solution import Solution



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