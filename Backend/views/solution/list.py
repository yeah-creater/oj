from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Backend.models.solution.solution import Solution

from Backend.models.solution.serializers import SolutionListSerializer
from rest_framework.pagination import PageNumberPagination
from Backend.models.user.user import UserInfo
import math
class ListView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            solutions = Solution.objects.filter(show = True)
            if request.GET.get('user_id') != None:
                solutions = solutions.filter(user_id = int(request.GET.get('user_id')))
            if request.GET.get('problem_id') != None:
                solutions = solutions.filter(problem__id = int(request.GET.get('problem_id')))
            pg = PageNumberPagination()
            res = pg.paginate_queryset(solutions, request)
            data = SolutionListSerializer(res, many=True).data
            print(data)
            for i in range(0, len(data)):
                user_info = UserInfo.objects.get(user_id = data[i]['user_id'])
                data[i]['user_info_name'] = user_info.name
                data[i]['user_info_photo'] = user_info.photo
            return Response({
                'result':'success',
                'total':(int)(math.ceil(len(solutions)/pg.page_size)*10),
                'data':data
            })
        except:
            return Response({
                'result': "fail",
                'data':'输入参数错误',
            })
