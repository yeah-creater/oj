from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.solution.solution import Solution
from Backend.models.blog.blog import Blog
from Backend.models.file.serializers import CommentSerializer
from rest_framework.pagination import PageNumberPagination
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoSerializer
from Backend.models.file.file import File
from Backend.models.file.file import Comment
from Backend.utils.find_file_id import find

import math
import json
class CommentView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            if (request.GET.get('type') == 'solution'):
                file_id = find('solution',request.GET.get('solution_id'))
                if file_id == 0:
                    return Response({
                    'result': "fail",
                    })
            elif (request.GET.get('type') == 'blog'):
                file_id = find('blog',request.GET.get('blog_id'))
                if file_id == 0:
                    return Response({
                    'result': "fail",
                    })
            elif (request.GET.get('type') == 'video'):
                file_id = find('video',request.GET.get('video_id'))
                if file_id == 0:
                    return Response({
                    'result': "fail",
                    })
            elif (request.GET.get('type') == 'contest'):
                file_id = find('contest',request.GET.get('contest_id'))
                if file_id == 0:
                    return Response({
                    'result': "fail",
                    })
            else:
                return Response({
                    'result': "输入参数错误",
                    })
            user_id = request.GET.get('user_id')
            user_infox = {
                'id':0,
                'username':'',
                'address':'',
                'avatar':'',
                'level':1,
                'likeIds':[],
            }
            user_infos = UserInfo.objects.filter(user_id = user_id)
            if user_infos.exists():
                t = user_infos[0]
                user_infox['id'] = t.user_id
                user_infox['username'] = t.name
                user_infox['address'] = t.address
                user_infox['avatar'] = t.photo
                user_infox['level'] = t.level
            comments = Comment.objects.filter(file_id = file_id,parentId = 0)
            data = CommentSerializer(comments, many=True).data
            for i in range(0, len(data)):
                user_id = data[i]['uid']
                user_info = UserInfo.objects.get(user_id = user_id)
                data[i]['user']={
                    'username':user_info.name,
                    'avatar':user_info.photo,
                    'level':user_info.level,
                    'homeLink':'/user/myspace/'+str(user_id)+'/'
                }
                total = 0
                sub_comments = Comment.objects.filter(file_id = file_id,parentId = data[i]['id'])
                total = len(sub_comments)
                sub_data = CommentSerializer(sub_comments, many=True).data
                for j in range(0, len(sub_data)):
                    sub_user_id = sub_data[j]['uid']
                    sub_user_info = UserInfo.objects.get(user_id = sub_user_id)
                    sub_data[j]['user']={
                        'username':sub_user_info.name,
                        'avatar':sub_user_info.photo,
                        'level':sub_user_info.level,
                        'homeLink':'/user/myspace/'+str(sub_user_id)+'/'
                    }
                data[i]['reply']={
                    'total':total,
                    'list':sub_data,
                }
            user_info_str = json.dumps(user_infox)
            return Response({
                'result': "success",
                'data':data,
                'user_info':user_info_str,
            })
        except:
            return Response({
                'result': "error",
            })
