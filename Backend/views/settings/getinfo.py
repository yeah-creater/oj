from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoSerializer

class GetInfoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            user_id = int(request.user.id)
            user = User.objects.get(id = user_id)
            user_info = user.user_info
            if user_info.forbidden:
                return Response({
                'result':'用户已被封禁',
                })
            serializer = UserInfoSerializer(user_info)
            return Response({
                'result':'success',
                'data':serializer.data,
            })
        except:
            return Response({
                'result': "输入参数错误"
            })
