from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.solution.solution import Solution
from Backend.models.blog.blog import Blog
from Backend.models.file.serializers import CommentSerializer
from rest_framework.pagination import PageNumberPagination
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoSerializer
from Backend.models.file.file import File
from Backend.models.file.file import Comment
from Backend.utils.find_file_id import find
from Backend.utils.comment_filter import query
class OperationView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        try:
            # if not query(request.POST.get('content')):
            #     return Response({
            #         'result': "该评论涉及冒犯性语言，请重新评论~~~",
            #     })
            user_id = request.user.id
            if request.POST.get('type') == 'solution':
                file_id = find('solution',request.POST.get('solution_id'))
                if file_id == 0:
                    return Response({
                    'result': "fail",
                    })
            elif request.POST.get('type') == 'blog':
                file_id = find('blog',request.POST.get('blog_id'))
                if file_id == 0:
                    return Response({
                    'result': "fail",
                    })
            elif request.POST.get('type') == 'video':
                file_id = find('video',request.POST.get('video_id'))
                if file_id == 0:
                    return Response({
                    'result': "fail",
                    })
            elif request.POST.get('type') == 'contest':
                file_id = find('contest',request.POST.get('contest_id'))
                if file_id == 0:
                    return Response({
                    'result': "fail",
                    })
            else:
                return Response({
                    'result':'输入参数错误',
                })
            data = request.POST
            parentId = int(data.get('parentId'))
            content = data.get('content')
            file = File.objects.get(id = file_id)
            address = UserInfo.objects.get(user_id = user_id).address
            comment = Comment.objects.create(file = file,uid = user_id,address = address,parentId = parentId,content = content)
            return Response({
                'result': "success",
                'data':comment.id
                })
        except:
            return Response({
                'result': "error",
            })
    def delete(self, request):
        try:
            user_id = request.user.id
            comment_id = request.POST.get('comment_id')
            comment = Comment.objects.get(id = comment_id)
            valid_user_id = comment.uid
            if user_id != valid_user_id:
                return Response({
                    'result':'无权限',
                })
            comment.delete()
            return Response({
                    'result':'success',
                })
        except:
            return Response({
                'result': "error",
            })
        
