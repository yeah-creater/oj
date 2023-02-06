from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.solution.solution import Solution
from Backend.models.solution.serializers import SolutionContentSerializer
from rest_framework.pagination import PageNumberPagination
from Backend.models.user.user import UserInfo
import math
class ContentView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        # try:
        solution = Solution.objects.filter(show = True)
        data = SolutionListSerializer(res).data
        for i in range(0, len(data)):
        user_info = UserInfo.objects.get(user_id = data[i]['user_id'])
        data[i]['user_info_name'] = user_info.name
        data[i]['user_info_photo'] = user_info.photo
        return Response({
            'result':'success',
            'data':data
        })
        # except:
        #     return Response({
        #         'result': "fail",
        #         'data':'输入参数错误',
        #     })
