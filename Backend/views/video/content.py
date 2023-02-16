from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.video.video import Video
from Backend.models.video.serializers import VideoContentSerializer
from Backend.models.user.user import UserInfo
from Backend.models.file.file import File
import math
class ContentView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            video_id = request.GET.get('video_id')
            if not Video.objects.filter(id = video_id,show = True).exists():
                return Response({
                'result':'fail',
                })
            video = Video.objects.get(id = video_id,show = True)
            content = video.file.content
            data = VideoContentSerializer(video).data
            user_info = UserInfo.objects.get(user_id = data['user_id'])
            data['user_info_name'] = user_info.name
            data['user_info_photo'] = user_info.photo
            data['content'] = content
            return Response({
                'result':'success',
                'data':data
            })
        except:
            return Response({
                'result': "error",
            })
