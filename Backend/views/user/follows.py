from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.user.user import UserInfo
from Backend.models.user.serializers import UserInfoSerializer

from Backend.models.user.user import Follow
from rest_framework.pagination import PageNumberPagination
import math
class FollowsView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        # try:
        data = request.GET
        if data['type'] == 'following':
            source = int(data['source'])
            s = set()
            followings = Follow.objects.filter(source = source)
            for f in followings:
                s.add(f.target)
            user_infoss = UserInfo.objects.all()
            user_infos=[]
            for user_info in user_infoss:
                if user_info.id in s:
                    user_infos.append(user_info)
            pg = PageNumberPagination()
            res = pg.paginate_queryset(user_infos,request)
            follows = UserInfoSerializer(res,many=True).data
        else:
            source = int(data['source'])
            s = set()
            followers = Follow.objects.filter(target = source)
            for f in followers:
                s.add(f.source)
            user_infoss = UserInfo.objects.all()
            user_infos=[]
            for user_info in user_infoss:
                if user_info.id in s:
                    user_infos.append(user_info)
            pg = PageNumberPagination()
            res = pg.paginate_queryset(user_infos,request)
            follows = UserInfoSerializer(res,many=True).data
        return Response({
            'result': "success",
            'data':follows,
            'total': (int)(math.ceil(len(user_infos)/pg.page_size)*10),
        })
        # except:
        #     return Response({
        #         'result': "fail",
        #     })
