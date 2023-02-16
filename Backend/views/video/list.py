from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.video.video import Video

from Backend.models.video.serializers import VideoListSerializer
from rest_framework.pagination import PageNumberPagination
from Backend.models.user.user import UserInfo
import math
class ListView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            videos = Video.objects.filter(show = True)
            if request.GET.get('problem_id') != None:
                videos = videos.filter(problem__id = int(request.GET.get('problem_id')))
            if videos.count() == 0:
                return Response({
                'result':'success',
                'total':0,
                'data':[],
            })
            pg = PageNumberPagination()
            res = pg.paginate_queryset(videos, request)
            data = VideoListSerializer(res, many=True).data
            for i in range(0, len(data)):
                user_info = UserInfo.objects.get(user_id = data[i]['user_id'])
                data[i]['user_info_name'] = user_info.name
                data[i]['user_info_photo'] = user_info.photo
            return Response({
                'result':'success',
                'total':(int)(math.ceil(len(videos)/pg.page_size)*10),
                'data':data
            })
        except:
            return Response({
                'result': "error",
            })
