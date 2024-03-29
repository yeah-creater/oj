from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Backend.models.user.user import UserInfo
from Backend.models.user.user import Follow
from Backend.models.notification.notification import Notification
class FollowView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        try:
            data = request.POST
            source_id = request.user.id
            target_id = int(data['target_id'])
            fs = Follow.objects.filter(source=source_id, target=target_id)
            if fs.exists():
                notification = Notification.objects.filter(notification_type ='关注了',source_id = target_id,target_id = source_id)
                if notification.exists():
                    notification.delete()
                user_info_target = UserInfo.objects.get(user_id = target_id)
                user_info_source = UserInfo.objects.get(user_id = source_id)
                user_info_target.followers -= 1
                user_info_source.followings -= 1
                user_info_target.save()
                user_info_source.save()
                fs.delete()
            else:
                notification = Notification.objects.filter(notification_type ='关注了',source_id = target_id,target_id = source_id)
                if not notification.exists():
                    Notification.objects.create(notification_type ='关注了',source_id = target_id,target_id = source_id)
                user_info_target = UserInfo.objects.get(user_id = target_id)
                user_info_source = UserInfo.objects.get(user_id = source_id)
                user_info_target.followers += 1
                user_info_source.followings += 1
                user_info_target.save()
                user_info_source.save()
                Follow.objects.create(source=source_id, target=target_id)
            return Response({
                'result': "success",
            })
        except:
            return Response({
                'result': "error",
            })
