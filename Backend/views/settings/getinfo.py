from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoSerializer
from Backend.models.notification.notification import Notification
import datetime
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
            data = UserInfoSerializer(user_info).data
            data['notification_count'] = Notification.objects.filter(source_id = user_id, read = False).count()
            return Response({
                'result':'success',
                'data':data,
            })
        except:
            return Response({
                'result': "输入参数错误"
            })
    def post(self, request):
        try:
            data = request.POST
            user_infos = UserInfo.objects.filter(user_id = request.user.id)
            if UserInfo.objects.filter(name = data['name']).exists():
                return Response({
                'result': "昵称已存在"
                })
            user_infos.update(name = data['name'], gender = data['gender'],record = data['record'],sno=data['sno'])
            return Response({
                'result': "success"
            })
        except:
            return Response({
                'result': "error"
            })
