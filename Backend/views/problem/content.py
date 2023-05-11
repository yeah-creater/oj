from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from Backend.models.problem.problem import Problem
from Backend.models.problem.serializers import ProblemSerializer
from Backend.models.contest.contest import Contest
from Backend.models.contest.contest import ContestParticipant
import datetime
from Backend.utils.md_to_html import md_to_html

EXTENTIONS = [
    'markdown.extensions.extra',  # 增加额外的Markdown语法支持，如表格、代码块等
    'markdown.extensions.codehilite',  # 增加代码高亮支持
]
KEYS=('description','input_format','output_format','data_range',
'input_example','output_example')
class ContentView(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        # try:
        problem_content_id = int(request.GET.get('problem_content_id', 1))
        user_id = int(request.GET.get('user_id', 0))
        problems = Problem.objects.filter(id = problem_content_id)
        if(len(problems)==0 or not problems[0].show):
            return Response({
            'result': "输入参数错误"
            })
        # 当前比赛未开始或当前用户未报名
        now = datetime.datetime.now()
        problem = problems[0]
        over = Contest.objects.filter(id = problem.contest, over_time__lte = now).exists()
        # 竞赛题并且比赛未结束
        if problem.contest != 0 and not over:
            r1 = Contest.objects.filter(id = problem.contest,start_time__lte = now).exists()
            r2 = ContestParticipant.objects.filter(contest_id = problem.contest,user_id = user_id).exists()
            # 未开始或未报名就不返回
            if not r1 or not r2:
                return Response({
                'result':'fail',
            })
        serializer = ProblemSerializer(problem)
        data = serializer.data
        for key in KEYS:
            val = data.get(key)
            data[key]=md_to_html(val)
        return Response({
            'result':'success',
            'data':data,
        })
        # except:
        #     return Response({
        #         'result': "error"
        #     })
