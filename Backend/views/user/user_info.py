from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoSerializer
from Backend.models.user.user import Follow
class UserInfoView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id'),0)
            visit_id = int(request.GET.get('visit_id'),0)
            visit_infos = UserInfo.objects.filter(id = visit_id)
            follows = Follow.objects.all()
            if len(visit_infos) == 0:
                return Response({
                'result': "输入参数错误"
                })
            visit_info = visit_infos[0]
            serializer = UserInfoSerializer(visit_info)
            data = serializer.data
            data['is_me'] = user_id == visit_id
            # 关注数
            data['followings'] = visit_info.followings
            # 粉丝数
            data['followers'] = visit_info.followers
            data['is_follow'] = follows.filter(source = user_id,target = visit_id).count() >= 1
            return Response({
                'result': "success",
                'data':data,
            })
        except:
            return Response({
                'result': "fail",
            })
