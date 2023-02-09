from rest_framework import serializers
from Backend.models.file.file import Comment



class CommentSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    class Meta:
        model = Comment
        fields = '__all__'