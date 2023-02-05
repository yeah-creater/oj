from rest_framework import serializers
from Backend.models.problem.problem import Problem

    

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id','title','difficulty']
class ProblemTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id','title']