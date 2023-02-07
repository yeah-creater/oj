from rest_framework import serializers
from Backend.models.blog.blog import Blog



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

