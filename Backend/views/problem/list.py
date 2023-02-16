from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.problem.problem import Problem
from Backend.models.problem.serializers import ProblemSerializer
from Backend.models.problem.serializers import ProblemListSerializer
from rest_framework.pagination import PageNumberPagination
import math
class ListView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        # try:
        problems = Problem.objects.filter(show = True)
        pg = PageNumberPagination()
        res = pg.paginate_queryset(problems,request)
        serializer = ProblemListSerializer(res,many=True)
        return Response({
            'result':'success',
            'total':(int)(math.ceil(len(problems)/pg.page_size)*10),
            'data':serializer.data,
        })
        # except:
        #     return Response({
        #         'result': "error",
        #     })
