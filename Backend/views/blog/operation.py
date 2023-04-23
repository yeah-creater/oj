from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Backend.models.blog.blog import Blog
from Backend.models.problem.problem import Problem
from Backend.models.user.user import UserInfo
from Backend.models.file.file import File
import math
class OperationView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        try:
            data = request.POST
            user_id = request.user.id
            if data.get('tags').strip() == '' or data.get('title').strip() == '':
                return Response({
                    'result': "请输入标签和标题",
                })
            tags = data.get('tags')
            title = data.get('title','').strip()
            content = data.get('content','')
            file = File.objects.create(content = content)
            Blog.objects.create(file = file,user_id = user_id,title = title,tags=tags)
            return Response({
                'result': "success",
            })
        except:
            return Response({
                'result': "error",
            })
    def delete(self, request):
        try:
            data = request.POST
            user_id = request.user.id
            blog_id = data.get('blog_id')
            blog = Blog.objects.get(id = blog_id)
            if blog.user_id != user_id:
                return Response({
                'result': "fail",
                })
            blog.show = False
            blog.save()
            return Response({
                'result': "success",
                })
        except:
            return Response({
                'result': "error",
            })
    def put(self,request):
        data = request.POST
        user_id = request.user.id
        blog_id = int(data.get('blog_id',""))
        title = data.get('title','').strip()
        tags = data.get('tags')
        content = data.get('content','')
        if not Blog.objects.filter(id = blog_id,show = True).exists():
            return Response({
                'result': "fail",
            })
        blog = Blog.objects.get(id = blog_id)
        if blog.user_id != user_id:
            return Response({
                'result': "fail",
            })
        blog.title = title
        blog.file.content = content
        blog.tags = tags
        blog.save()
        blog.file.save()
        return Response({
                'result': "success",
            })
        