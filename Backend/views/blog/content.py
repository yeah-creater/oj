from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.blog.blog import Blog
from Backend.models.blog.serializers import BlogContentSerializer
from Backend.models.user.user import UserInfo
from Backend.utils.md_to_html import md_to_html
from Backend.models.file.file import File
import math
class ContentView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        blog_id = request.GET.get('blog_id')
        if not Blog.objects.filter(id = blog_id,show = True).exists():
            return Response({
            'result':'fail',
            })
        blog = Blog.objects.get(id = blog_id,show = True)
        data = BlogContentSerializer(blog).data
        user_info = UserInfo.objects.get(user_id = data['user_id'])
        content = blog.file.content
        data['user_info_name'] = user_info.name
        data['user_info_photo'] = user_info.photo
        data['content'] = content
        if int(request.GET.get('md')) == 0:
            data['content'] = md_to_html(content)
        return Response({
            'result':'success',
            'data':data
        })
